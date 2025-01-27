Name:           lexertl17
Summary:        The Modular Lexical Analyser Generator
# Upstream switched away from calendar-based versioning, and the new version
# scheme sorts older than the calendar-based one, so we cannot avoid an Epoch.
Epoch:          1
Version:        1.1.3
Release:        %autorelease

# The entire source is BSL-1.0, except that the following are Unicode-3.0:
# - gen_unicode_hpp/Blocks.txt
# - gen_unicode_hpp/Scripts.txt
# - gen_unicode_hpp/UnicodeData.txt
# Since these are used to generate:
# - include/lexertl/parser/tokeniser/unicode.hpp
# …it is possibly Unicode-3.0 as well.
License:        BSL-1.0 AND Unicode-3.0
URL:            https://github.com/BenHanson/lexertl17
Source:         %{url}/archive/%{version}/lexertl17-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  dos2unix

# No compiled binaries are installed, so this would be empty.
%global debug_package %{nil}

%global common_description %{expand:
lexertl is a header-only library for writing lexical analyzers. With lexertl
you can:

- Build lexical analyzers at runtime
- Scan Unicode and ASCII input
- Scan from files or memory
- Generate C++ code or even write your own code generator}

%description %{common_description}


%package devel
Summary:        %{summary}

# Header-only library:
Provides:       lexertl17-static = %{epoch}:%{version}-%{release}
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Conflicts/#_compat_package_conflicts
Conflicts:      lexertl14-devel

%description devel %{common_description}


%prep
%autosetup -n lexertl17-%{version}

# Fix line terminations (particularly for files that may be installed)
find . -type f -exec file '{}' '+' |
  grep -E '\bCRLF\b' |
  cut -d ':' -f 1 |
  xargs -r dos2unix --keepdate


%conf
%cmake -DBUILD_TESTING:BOOL=ON -DBUILD_EXAMPLES:BOOL=ON


%build
%cmake_build

# Make a copy of the examples directory without CMakeLists.txt files, which are
# not useful without the top-level CMakeLists.txt for the project.
mkdir _cleaned
cp -rvp examples _cleaned
find _cleaned/examples -type f -name CMakeLists.txt -print -delete


%install
%cmake_install


%check
%ctest


%files devel
%license include/lexertl/licence_1_0.txt
%doc README.md
%doc _cleaned/examples/

%{_includedir}/lexertl/

%{_libdir}/cmake/lexertl/


%changelog
%autochangelog
