%global commit 98231f9a0bcd60038cc542c83a8f639017911b3f
%global snapdate 20260418

Name:           lexertl14
Summary:        The Modular Lexical Analyser Generator
Version:        0.1.0^%{snapdate}.%{sub %{commit} 1 7}
Epoch:          1
Release:        %autorelease

License:        BSL-1.0
URL:            https://github.com/BenHanson/lexertl14
Source:         %{url}/archive/%{commit}/lexertl14-%{commit}.tar.gz

BuildSystem:    cmake

BuildRequires:  gcc-c++
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
Provides:       lexertl14-static = %{epoch}:%{version}-%{release}
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Conflicts/#_compat_package_conflicts
Conflicts:      lexertl17-devel

Obsoletes:      lexertl14-examples < 0.1.0^20240216git7a365a2-5

%description devel %{common_description}


%prep -a
# Fix line terminations (particularly for files that may be installed)
find . -type f -exec file '{}' '+' |
  grep --regexp-extended '\bCRLF\b' |
  cut --delimiter=':' --fields=1 |
  xargs --no-run-if-empty dos2unix --keepdate


%files devel
%license include/lexertl/licence_1_0.txt
%doc README.md

%{_includedir}/lexertl/

%{_libdir}/cmake/lexertl/


%changelog
%autochangelog
