Name:           gram_grep
Summary:        Search text using a grammar, lexer, or straight regex
Version:        0.10.2
Release:        %autorelease

# Since dependencies lexertl17, parsertl17, and wildcardtl are header-only, we
# must treat them as static libraries, and their licenses contribute to the
# license of the binary RPM. All three are BSL-1.0.
License:        BSL-1.0
URL:            https://github.com/BenHanson/gram_grep
Source0:        %{url}/archive/%{version}/gram_grep-%{version}.tar.gz
# Man page hand-written for Fedora in groff_man(7) format based on --help
Source1:        gram_grep.1

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  dos2unix

BuildRequires:  boost-devel
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
%cmake


%build
%cmake_build


%install
# The CMake build system has no provision for installing the program, so
# %%cmake_install would do nothing. We must install the executable manually.
install -t '%{buildroot}%{_bindir}' -p -D %{_vpath_builddir}/gram_grep
install -t '%{buildroot}%{_mandir}/man1' -p -D -m 0644 '%{SOURCE1}'


%check
# Upstream does not provide any tests. We use the “Printing a Reversed List”
# example from README.md as a “smoke test.”

# Make sure the program can at least print its help text and exit successfully
%{buildroot}%{_bindir}/gram_grep --help >/dev/null

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

printf '%s\n' 'a::b::c::d' > test.txt
expected='d::c::b::a'
assert_same "$(set -o errexit
  %{buildroot}%{_bindir}/gram_grep --config=sample_configs/rev.g test.txt
)" "${expected}"


%files
%license LICENCE.txt
%doc README.md
%doc sample_configs/

%{_bindir}/gram_grep
%{_mandir}/man1/gram_grep.1*


%changelog
%autochangelog
