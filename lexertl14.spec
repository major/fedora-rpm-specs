%global commit 86c90c37dd69ee45155d11e38a77b21eac5dccbe
%global snapdate 20230904

Name:           lexertl14
Summary:        The Modular Lexical Analyser Generator
Version:        0.1.0^%{snapdate}git%(c='%{commit}'; echo "${c:0:7}")
Release:        %autorelease

License:        BSL-1.0
URL:            https://github.com/BenHanson/lexertl14
Source:         %{url}/archive/%{commit}/lexertl14-%{commit}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  dos2unix

# No compiled binaries are installed, so this would be empty.
%global debug_package %{nil}

%global common_description %{expand:
lexertl is a header-only library for writing lexical analysers. With lexertl
you can:

  • Build lexical analysers at runtime
  • Scan Unicode and ASCII input
  • Scan from files or memory
  • Generate C++ code or even write your own code generator}

%description %{common_description}


%package devel
Summary:        %{summary}

# Header-only library:
Provides:       lexertl14-static = %{version}-%{release}

%description devel %{common_description}


%package examples
Summary:        Examples for lexertl14
BuildArch:      noarch

%description examples
%{summary}.


%prep
%autosetup -n lexertl14-%{commit}
# Adapt to multilib:
sed -r -i 's@(DESTINATION )lib\b@\1%{_libdir}@' CMakeLists.txt
# Fix line terminations (particularly for files that may be installed)
find . -type f -exec file '{}' '+' |
  grep -E '\bCRLF\b' |
  cut -d ':' -f 1 |
  xargs -r dos2unix
# sed -r -i 's@\(test\)@\(tests/fail_tests\)@' CMakeLists.txt


%build
%cmake -DBUILD_TESTING:BOOL=on
%cmake_build


%install
%cmake_install


%check
%ctest


%files devel
%license include/lexertl/licence_1_0.txt
%doc README.md

%{_includedir}/lexertl/

%{_libdir}/cmake/lexertl/


%files examples
%license include/lexertl/licence_1_0.txt
%doc examples/*


%changelog
%autochangelog
