%{?scl:%scl_package pgaudit}
%{!?scl:%global pkg_name %{name}}

Name:		%{?scl_prefix}pgaudit
Version:	1.3.1
Release:	1%{?dist}
Summary:	PostgreSQL Audit Extension

License:	PostgreSQL
URL:		http://pgaudit.org

Source0:	https://github.com/%{pkg_name}/%{pkg_name}/archive/%{version}/%{pkg_name}-%{version}.tar.gz
Patch0:		%{pkg_name}-pgsql12compat.patch

%{?scl:Requires: %{scl}-runtime}
%{?scl:BuildRequires: %{scl}-runtime}
BuildRequires: gcc
BuildRequires: %{?scl_prefix}postgresql-devel >= 11, %{?scl_prefix}postgresql-devel < 13
BuildRequires: openssl-devel

%{?%rh_postgresql10_postgresql_module_requires}


%description
The PostgreSQL Audit extension (pgaudit) provides detailed session
and/or object audit logging via the standard PostgreSQL logging
facility.

The goal of the PostgreSQL Audit extension (pgaudit) is to provide
PostgreSQL users with capability to produce audit logs often required to
comply with government, financial, or ISO certifications.

An audit is an official inspection of an individual's or organization's
accounts, typically by an independent body. The information gathered by
the PostgreSQL Audit extension (pgaudit) is properly called an audit
trail or audit log. The term audit log is used in this documentation.


%prep
%{?scl:scl enable %{scl} - << \EOF}
set -ex
%setup -q -n %{pkg_name}-%{version}
%patch0 -p1 -b .pgsql12compat
%{?scl:EOF}


%build
%{?scl:scl enable %{scl} - << \EOF}
set -ex
%{__make} USE_PGXS=1 %{?_smp_mflags}
%{?scl:EOF}


%install
%{?scl:scl enable %{scl} - << \EOF}
set -ex
%{__make}  USE_PGXS=1 %{?_smp_mflags} DESTDIR=$RPM_BUILD_ROOT install
%{?scl:EOF}


%files
%doc README.md
%license LICENSE
%{_libdir}/pgsql/%{pkg_name}.so
%{_datadir}/pgsql/extension/%{pkg_name}--1*.sql
%{_datadir}/pgsql/extension/%{pkg_name}.control


%changelog
* Sat Jul 27 2019 Honza Horak <hhorak@redhat.com> - 1.3.1-1
- Update to 1.3.1 and apply patch for pgsql v12 compatibility

* Thu Jul 25 2019 Honza Horak <hhorak@redhat.com> - 1.2.0-4
- SCLize the SPEC

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Dec 20 2017 - Filip Čáp <ficap@redhat.com> 1.2.0-1
- Initial RPM packaging for Fedora
- Based on Devrim Gündüz's packaging for PostgreSQL RPM Repo

* Thu Oct 27 2016 - Devrim Gündüz <devrim@gunduz.org> 1.0.0-1
- Update to 1.0.0

* Fri Oct 21 2016 - Devrim Gündüz <devrim@gunduz.org> 0.0.4-1
- Initial RPM packaging for PostgreSQL RPM Repository
