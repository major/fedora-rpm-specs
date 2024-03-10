Name:           parsertl17
Summary:        The Modular Parser Generator
Version:        2024.02.17
Release:        %autorelease

License:        BSL-1.0
URL:            https://github.com/BenHanson/parsertl17
Source:         %{url}/archive/%{version}/parsertl17-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  dos2unix

BuildRequires:  lexertl17-devel
# Header-only library:
# (Technically, dependent packages should have this BuildRequires too.)
BuildRequires:  lexertl17-static

# No compiled binaries are installed, so this would be empty.
%global debug_package %{nil}

%global common_description %{expand:
%{summary}.}

%description %{common_description}


%package devel
Summary:        %{summary}

BuildArch:      noarch

# Header-only library:
Provides:       parsertl17-static = %{version}-%{release}
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Conflicts/#_compat_package_conflicts
Conflicts:      parsertl14-devel

Requires:       lexertl17-devel

%description devel %{common_description}


%prep
%autosetup -n parsertl17-%{version}

# Fix line terminations (particularly for files that may be installed)
find . -type f -exec file '{}' '+' |
  grep -E '\bCRLF\b' |
  cut -d ':' -f 1 |
  xargs -r dos2unix --keepdate


# Nothing to build


%install
install -d '%{buildroot}%{_includedir}'
cp -rvp include/parsertl '%{buildroot}%{_includedir}/'


%check
%set_build_flags
${CXX-g++} -I"${PWD}/include" ${CPPFLAGS} ${CXXFLAGS} -o include_test ${LDFLAGS} \
    tests/include_test/*.cpp


%files devel
%license include/parsertl/licence_1_0.txt
%doc README.md

%{_includedir}/parsertl/


%changelog
%autochangelog
