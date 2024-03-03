# Post-release snapshot with fixes for examples
# https://github.com/BenHanson/lexertl17/pull/2
# https://github.com/BenHanson/lexertl17/commit/fc939f3d401753caa4c4c8b4442b169d7fef584d
%global commit fc939f3d401753caa4c4c8b4442b169d7fef584d
%global snapdate 20240301

Name:           lexertl17
Summary:        The Modular Lexical Analyser Generator
Version:        2024.02.17%{?commit:^%{snapdate}git%{sub %{commit} 1 7}}
Release:        %autorelease

License:        BSL-1.0
URL:            https://github.com/BenHanson/lexertl17
%global srcversion %{?!commit:%{version}}%{?commit:%{commit}}
Source:         %{url}/archive/%{srcversion}/lexertl17-%{srcversion}.tar.gz

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
Provides:       lexertl17-static = %{version}-%{release}
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Conflicts/#_compat_package_conflicts
Conflicts:      lexertl14-devel

%description devel %{common_description}


%prep
%autosetup -n lexertl17-%{srcversion}

# Fix line terminations (particularly for files that may be installed)
find . -type f -exec file '{}' '+' |
  grep -E '\bCRLF\b' |
  cut -d ':' -f 1 |
  xargs -r dos2unix --keepdate


%build
%cmake -DBUILD_TESTING:BOOL=ON -DBUILD_EXAMPLES:BOOL=ON
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
