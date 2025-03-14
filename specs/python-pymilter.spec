# we don't want to provide private python extension libs
%global sum Python interface to sendmail milter API
%global __provides_exclude_from ^(%{python2_sitearch})/.*\\.so$
%if 0%{?fedora} >= 32
%bcond_with python2
%global python2 python27
%else
%if 0%{?epel} < 8
%bcond_without python2
%else
%bcond_with python2
%endif
%global python2 python2
%endif

Summary: %{sum}
Name: python-pymilter
Version: 1.0.6
Release: %autorelease
Url:    https://www.pymilter.org
Source: https://github.com/sdgathman/pymilter/archive/pymilter-%{version}.tar.gz
#       https://github.com/sdgathman/pymilter/tags
Source1: tmpfiles-python-pymilter.conf
# remove unit tests that require network for check
Patch0: pymilter-check.patch
# Apply patch replacing deprecated makeSuite() (removed from Python 3.13)
Patch1: https://github.com/sdgathman/pymilter/pull/65.patch
# Use C17 for compilation (fails with C23; default in GCC 15)
Patch2: https://github.com/sdgathman/pymilter/pull/70.patch
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License: GPL-2.0-or-later
Group: Development/Libraries
BuildRequires: python%{python3_pkgversion}-devel, sendmail-devel >= 8.13
# python-2.6.4 gets RuntimeError: not holding the import lock
# Need python2.6 specific pydns, not the version for system python
BuildRequires:  gcc
BuildRequires:  python%{python3_pkgversion}-bsddb3

%global _description\
This is a python extension module to enable python scripts to\
attach to sendmail's libmilter functionality.  Additional python\
modules provide for navigating and modifying MIME parts, sending\
DSNs, and doing CBV.

%description %_description

%if %{with python2}
%package -n %{python2}-pymilter
Summary: %{sum}
%if 0%{?epel} >= 6 && 0%{?epel} < 8
Requires: python-pydns
%else
Requires: %{python2}-pydns
%endif
Requires: %{name}-common = %{version}-%{release}
%{?python_provide:%python_provide %{python2}-pymilter}
BuildRequires: %{python2}-devel

%description -n python2-pymilter %_description
%endif

%package -n python%{python3_pkgversion}-pymilter
Summary: %{sum}
%if 0%{?fedora} >= 26
Requires: python%{python3_pkgversion}-py3dns
%endif
Requires: %{name}-common = %{version}-%{release}
%{?python_provide:%python_provide python%{python3_pkgversion}-pymilter}

%description -n python%{python3_pkgversion}-pymilter %_description

%package common
Summary: Common files and directories for python milters
BuildArch: noarch

%description common
Common files and directories used for python milters

%package selinux
Summary: SELinux policy module for pymilter
Group: System Environment/Base
Requires: policycoreutils, selinux-policy-targeted
Requires: %{name}-common = %{version}-%{release}
BuildArch: noarch
BuildRequires: policycoreutils, checkpolicy, selinux-policy-devel
%if 0%{?epel} >= 6 && 0%{?epel} < 8
BuildRequires: policycoreutils-python
%else
BuildRequires: policycoreutils-python-utils
%endif

%description selinux
Give sendmail_t additional access to stream sockets used to communicate
with milters.

%prep
%setup -q -n pymilter-pymilter-%{version}
#setup -q -n pymilter-%%{version}
%patch -P0 -p1 -b .check
%patch -P1 -p1 -b .check
%patch -P2 -p1 -b .check
cp -p template.py milter-template.py


%build
%if %{with python2}
%py2_build
%endif
%py3_build
checkmodule -m -M -o pymilter.mod pymilter.te
semodule_package -o pymilter.pp -m pymilter.mod

%install
%if %{with python2}
%py2_install
%endif
%py3_install

mkdir -p %{buildroot}/run/milter
mkdir -p %{buildroot}%{_localstatedir}/log/milter
mkdir -p %{buildroot}%{_libexecdir}/milter
mkdir -p %{buildroot}%{_prefix}/lib/tmpfiles.d
install -m 0644 %{SOURCE1} %{buildroot}%{_prefix}/lib/tmpfiles.d/%{name}.conf

# install selinux modules
mkdir -p %{buildroot}%{_datadir}/selinux/targeted
cp -p pymilter.pp %{buildroot}%{_datadir}/selinux/targeted

%check
%if %{with python2}
py2path=$(ls -d build/lib.linux-*-2.*)
PYTHONPATH=${py2path}:. python2 test.py &&
%endif
py3path=$(ls -d build/lib.linux-*-3*)
PYTHONPATH=${py3path}:. python3 test.py

%if %{with python2}
%files -n %{python2}-pymilter
%license COPYING
%doc README.md ChangeLog NEWS TODO CREDITS sample.py milter-template.py
%{python2_sitearch}/*
%endif

%files -n python%{python3_pkgversion}-pymilter
%license COPYING
%doc README.md ChangeLog NEWS TODO CREDITS sample.py milter-template.py
%{python3_sitearch}/*

%files common
%dir %{_libexecdir}/milter
%{_prefix}/lib/tmpfiles.d/%{name}.conf
%dir %attr(0755,mail,mail) %{_localstatedir}/log/milter
%dir %attr(0755,mail,mail) /run/milter

%files selinux
%doc pymilter.te
%{_datadir}/selinux/targeted/*

%post selinux
%{_sbindir}/semodule -s targeted -i %{_datadir}/selinux/targeted/pymilter.pp \
        &>/dev/null || :

%postun selinux
if [ $1 -eq 0 ] ; then
%{_sbindir}/semodule -s targeted -r pymilter &> /dev/null || :
fi

%changelog
%autochangelog
