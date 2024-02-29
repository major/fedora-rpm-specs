%global commit 7a365a26777c4d4de47e5d8db7e68f0974db5e20
%global snapdate 20240216

Name:           lexertl14
Summary:        The Modular Lexical Analyser Generator
Version:        0.1.0^%{snapdate}git%{sub %{commit} 1 7}
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
This is the C++14 version of lexertl. Please prefer lexertl17 wherever
possible.}

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
%autosetup -n lexertl14-%{commit} -p1
# Fix line terminations (particularly for files that may be installed)
find . -type f -exec file '{}' '+' |
  grep -E '\bCRLF\b' |
  cut -d ':' -f 1 |
  xargs -r dos2unix --keepdate


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
