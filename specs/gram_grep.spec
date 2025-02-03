Name:           gram_grep
Summary:        Search text using a grammar, lexer, or straight regex
Version:        0.9.0
Release:        %autorelease

# Since dependencies lexertl17, parsertl17, and wildcardtl are header-only, we
# must treat them as static libraries, and their licenses contribute to the
# license of the binary RPM. All three are BSL-1.0.
License:        BSL-1.0
URL:            https://github.com/BenHanson/gram_grep
Source0:        %{url}/archive/%{version}/gram_grep-%{version}.tar.gz
# Man page hand-written for Fedora in groff_man(7) format based on --help
Source1:        gram_grep.1
# Main source file as of version 0.9.0; we use this for “smoke testing,” so we
# need a copy that does not change every time we ship an update. This does
# *not* contribute to the binary RPMs.
Source2:        main-0.9.0.cpp

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  gcc-c++
BuildRequires:  cmake
# Ninja is a little faster than make and has no disadvantages.
BuildRequires:  ninja-build
BuildRequires:  dos2unix

# https://docs.fedoraproject.org/en-US/packaging-guidelines/#_packaging_header_only_libraries
BuildRequires:  lexertl17-static
BuildRequires:  parsertl17-static
BuildRequires:  wildcardtl-static

%description
Search text using a grammar, lexer, or straight regex. Chain searches for
greater refinement.


%prep
%autosetup -n gram_grep-%{version}

# Fix line terminations (particularly for files that may be installed)
find . -type f -exec file '{}' '+' |
  grep -E '\bCRLF\b' |
  cut -d ':' -f 1 |
  xargs -r dos2unix --keepdate

# Remove include paths for unbundled header-only library dependencies
sed -r -i 's@^([[:blank:]]*)(include_directories.*"\.\./)@\1# \2@' \
    CMakeLists.txt


%conf
%cmake -GNinja


%build
%cmake_build


%install
# The CMake build system has no provision for installing the program, so
# %%cmake_install would do nothing. We must install the executable manually.
install -t '%{buildroot}%{_bindir}' -p -D %{_vpath_builddir}/gram_grep
install -t '%{buildroot}%{_mandir}/man1' -p -D -m 0644 '%{SOURCE1}'


%check
# Upstream does not provide any tests. We use a few of the examples from
# http://benhanson.net/gram_grep.html as “smoke tests.”

# Make sure the program can at least print its help text and exit successfully
%{buildroot}%{_bindir}/gram_grep --help >/dev/null

# Copy in a fixed version of main.cpp (as of version 0.9.0) as a sample file to
# process. By doing this instead of operating on the actual main.cpp, the
# output from our “smoke tests” does not change with each update.
cp -p '%{SOURCE2}' _x.cpp

assert_same() {
  # Parameters: actual, expected
  set -o nounset
  set -o errexit
  if [ "${1}" != "${2}" ]
  then
    cat 1>&2 <<EOF
==== Actual ====
${1}
==== Expected ====
${2}
EOF
    exit 1
  fi
}

expected='_x.cpp:15:#include <lexertl/memory_file.hpp>
_x.cpp:616:    lexertl::memory_file& mf,
_x.cpp:783:    lexertl::memory_file mf(pathname.c_str());
_x.cpp:1348:            lexertl::memory_file& mf ='

assert_same "$(set -o errexit
  %{buildroot}%{_bindir}/gram_grep -Hn -v \
      --flex-regexp "\/\/.*|\/\*(?s:.)*?\*\/" -F memory_file _x.cpp
)" "${expected}"
# Same search with a config file:
assert_same "$(set -o errexit
  %{buildroot}%{_bindir}/gram_grep -Hn --config=sample_configs/nosc.g _x.cpp
)" "${expected}"


%files
%license LICENCE.txt
%doc README.md
%doc sample_configs/

%{_bindir}/gram_grep
%{_mandir}/man1/gram_grep.1*


%changelog
%autochangelog
