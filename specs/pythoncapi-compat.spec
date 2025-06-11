%global commit ffae0ffa2a3f906fd471e2d672731205f7e5febd
%global snapdate 20250609

Name:           pythoncapi-compat
Summary:        Python C API compatibility
# Upstream has never versioned this project.
Version:        0^%{snapdate}git%{sub %{commit} 1 7}
Release:        %autorelease

License:        0BSD
URL:            https://github.com/python/pythoncapi-compat
Source0:        %{url}/archive/%{commit}/pythoncapi-compat-%{commit}.tar.gz
# Man page hand-written for Fedora in groff_man(7) format based on --help
Source1:        upgrade_pythoncapi.py.1

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  python3-devel

# As a header-only library package (with an additional command-line tool
# subpackage), the base package is arched so that it is compiled and tested on
# all architectures; however, no compiled code is installed, and there are no
# debugging symbols.
%global debug_package %{nil}

%global common_description %{expand:
The pythoncapi-compat project can be used to write a C or C++ extension
supporting a wide range of Python versions with a single code base. It is made
of the pythoncapi_compat.h header file and the upgrade_pythoncapi.py script.}

%description %{common_description}


%package devel
Summary:        %{summary}

# https://docs.fedoraproject.org/en-US/packaging-guidelines/#_packaging_header_only_libraries
Provides:       pythoncapi-compat-static = %{version}-%{release}

BuildArch:      noarch

%description devel %{common_description}

This package provides the compatibility header library pythoncapi_compat.h.


%package tools
Summary:        %{summary}

BuildArch:      noarch

%description tools %{common_description}

This package provides the command-line tool upgrade_pythoncapi.py.


%package doc
Summary:        Documentation for pythoncapi-compat

BuildArch:      noarch

%description doc %{common_description}


%prep
%autosetup -n pythoncapi-compat-%{commit}
# Compiling with -Werror makes sense for upstream CI, but is probably too
# brittle for downstream builds.
sed -r -i "s/^([[:blank:]]*)(['\"]-Werror)/\1# \2/" tests/setup.py


%generate_buildrequires
pushd tests >/dev/null
%pyproject_buildrequires
popd >/dev/null


%build
pushd tests >/dev/null
%pyproject_wheel
popd >/dev/null


%install
install -t '%{buildroot}%{_includedir}' -D -p -m 0644 pythoncapi_compat.h
install -D -p -t '%{buildroot}%{_bindir}' upgrade_pythoncapi.py
install -t '%{buildroot}%{_mandir}/man1' -D -p -m 0644 '%{SOURCE1}'
%py3_shebang_fix %{buildroot}%{_bindir}/upgrade_pythoncapi.py


%check
%{py3_test_envvars} %{python3} runtests.py --current --verbose


%files devel
%license COPYING

%{_includedir}/pythoncapi_compat.h


%files tools
%license COPYING

%{_bindir}/upgrade_pythoncapi.py
%{_mandir}/man1/upgrade_pythoncapi.py.1*


%files doc
%license COPYING

# This primarily documents the script rather than the header.
%doc README.rst

%doc docs/*.rst


%changelog
%autochangelog
