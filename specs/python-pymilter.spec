Name:           python-pymilter
Version:        1.0.6
Release:        %autorelease
Summary:        Python interface to sendmail milter API
Group:          Development/Libraries

License:        GPL-2.0-or-later
URL:            https://www.pymilter.org
Source:         https://github.com/sdgathman/pymilter/archive/pymilter-%{version}.tar.gz
# https://github.com/sdgathman/pymilter/tags
Source1:        tmpfiles-python-pymilter.conf
# remove unit tests that require network for check
Patch0:         pymilter-check.patch
# Apply patch replacing deprecated makeSuite() (removed from Python 3.13)
Patch1:         https://github.com/sdgathman/pymilter/pull/65.patch
# Use C17 for compilation (fails with C23; default in GCC 15)
Patch2:         https://github.com/sdgathman/pymilter/pull/70.patch

BuildRequires:  gcc
BuildRequires:  python3-devel
# One test reads from a Berkeley DB file. It works with either
# berkeleydb or bsddb3.
BuildRequires:  (python3-berkeleydb or python3-bsddb3)
# For /usr/bin/makemap required by testpolicy.py
BuildRequires:  sendmail
BuildRequires:  sendmail-milter-devel >= 8.13

%global _description %{expand:
This is a python extension module to enable python scripts to attach to
sendmail's libmilter functionality.  Additional python modules provide
for navigating and modifying MIME parts, sending DSNs, and doing CBV.}

%description %_description

%package -n python3-pymilter
Summary:        %{summary}

Requires:       python3-py3dns
Requires:       %{name}-common = %{version}-%{release}
%{?python_provide:%python_provide python3-pymilter}

%description -n python3-pymilter %_description

%package common
Summary:        Common files and directories for python milters
BuildArch:      noarch

%description common
Common files and directories used for python milters

%package selinux
Summary:        SELinux policy module for pymilter
Group:          System Environment/Base

Requires:       policycoreutils, selinux-policy-targeted
Requires:       %{name}-common = %{version}-%{release}

BuildArch:      noarch
BuildRequires:  checkpolicy
BuildRequires:  policycoreutils
BuildRequires:  policycoreutils-python-utils
BuildRequires:  selinux-policy-devel

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

# Fix version
# setup.py has not been updated in tag 1.0.6
# https://github.com/sdgathman/pymilter/blob/pymilter-1.0.6/setup.py
sed -r -i 's/1\.0\.5/%{version}/' setup.py

# Fix policy test
# https://github.com/sdgathman/pymilter/issues/62
sed -r -i 's/(access_file_nulls) *= *True/\1 = False/g' testpolicy.py


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel
checkmodule -m -M -o pymilter.mod pymilter.te
semodule_package -o pymilter.pp -m pymilter.mod


%install
%pyproject_install
%pyproject_save_files -l Milter milter mime

mkdir -p %{buildroot}/run/milter
mkdir -p %{buildroot}%{_localstatedir}/log/milter
mkdir -p %{buildroot}%{_libexecdir}/milter
mkdir -p %{buildroot}%{_prefix}/lib/tmpfiles.d
install -m 0644 %{SOURCE1} %{buildroot}%{_prefix}/lib/tmpfiles.d/%{name}.conf

# install selinux modules
mkdir -p %{buildroot}%{_datadir}/selinux/targeted
cp -p pymilter.pp %{buildroot}%{_datadir}/selinux/targeted


%check
%py3_test_envvars %python3 test.py


%files -n python3-pymilter -f %{pyproject_files}
%doc README.md ChangeLog NEWS TODO CREDITS sample.py milter-template.py

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
