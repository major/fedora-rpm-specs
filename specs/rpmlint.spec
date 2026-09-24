# pass --without tests to skip the test suite
%bcond_without tests

Name:           rpmlint
Version:        2.10.0
Release:        %autorelease
Summary:        Tool for checking common errors in RPM packages
License:        GPL-2.0-or-later
URL:            https://github.com/rpm-software-management/rpmlint
Source0:        %{url}/archive/%{version}/rpmlint-%{version}.tar.gz

# Taken from https://github.com/rpm-software-management/rpmlint/tree/main/configs/Fedora
Source1:        fedora.toml
Source3:        scoring.toml
Source4:        users-groups.toml
Source5:        warn-on-functions.toml

BuildArch:      noarch

# use git to apply patches; it handles binary diffs
BuildRequires:  git-core
BuildRequires:  python3-devel
# tests
%if %{with tests}
%if ! 0%{?rhel}
BuildRequires:  dash
%endif
BuildRequires:  devscripts-checkbashisms
BuildRequires:  hunspell-cs
BuildRequires:  hunspell-en-US
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-xdist)
BuildRequires:  /usr/bin/appstream-util
BuildRequires:  /usr/bin/desktop-file-validate
%endif
%if ! 0%{?rhel}
Requires:       dash
%endif
Requires:       devscripts-checkbashisms
Requires:       rpm-build
Requires:       /usr/bin/appstream-util
Requires:       /usr/bin/desktop-file-validate
Requires:       rpmlint-fedora-license-data
Requires:       glibc-langpack-en

%description
rpmlint is a tool for checking common errors in RPM packages. Binary
and source packages as well as spec files can be checked.

%prep
%autosetup -p1 -Sgit_am

# Replace python-magic dep with file-magic (rhbz#1899279)
sed -i 's/python-magic/file-magic/g' pyproject.toml

%if 0%{?rhel}
# Avoid extra dependencies for checks not needed in RHEL
# pybeam: ErlangCheck
sed -i -e '/pybeam/d' pyproject.toml
sed -i -e '/ErlangCheck/d' rpmlint/configdefaults.toml test/test_lint.py
%endif

# Don't lint the code or measure coverage in %%check
sed -i -e '/^ *--cov=rpmlint$/d' pytest.ini

# Avoid warnings about pytest.mark.no_cover marker
sed -i '/^@pytest.mark.no_cover/d' test/test_lint.py

if ! which dash checkbashisms >/dev/null; then
    # Disable bashisms check if dash or checkbashisms is unavailable.
    sed -i -e '/BashismsCheck/d' %{SOURCE1}
fi

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{name}

mkdir -p %{buildroot}%{_sysconfdir}/xdg/rpmlint/
cp -a %{SOURCE1} %{SOURCE3} %{SOURCE4} %{SOURCE5} %{buildroot}%{_sysconfdir}/xdg/rpmlint/

%check
%if %{with tests}
%pytest %{?rhel:--ignore test/test_erlang.py}
%endif

%files -f %{pyproject_files}
%doc README.md
%dir %{_sysconfdir}/xdg/rpmlint
%config(noreplace) %{_sysconfdir}/xdg/rpmlint/*.toml
%{_bindir}/rpmdiff
%{_bindir}/rpmlint

%changelog
%autochangelog
