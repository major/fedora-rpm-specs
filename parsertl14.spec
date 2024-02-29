%global commit f72113681dc5fe685b8814ed6cd5e768f93ed529
%global snapdate 20240215

Name:           parsertl14
Summary:        The Modular Parser Generator
# Upstream has never versioned the library.
Version:        0^%{snapdate}git%{sub %{commit} 1 7}
Release:        %autorelease

License:        BSL-1.0
URL:            https://github.com/BenHanson/parsertl14
Source:         %{url}/archive/%{commit}/parsertl14-%{commit}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  dos2unix

BuildRequires:  lexertl14-devel
# Header-only library:
# (Technically, dependent packages should have this BuildRequires too.)
BuildRequires:  lexertl14-static

# No compiled binaries are installed, so this would be empty.
%global debug_package %{nil}

%global common_description %{expand:
%{summary}.}

%description %{common_description}


%package devel
Summary:        %{summary}

BuildArch:      noarch

# Header-only library:
Provides:       parsertl14-static = %{version}-%{release}

Requires:       lexertl14-devel

%description devel %{common_description}


%prep
%autosetup -n parsertl14-%{commit} -p1

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
