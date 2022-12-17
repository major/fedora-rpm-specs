Name:           libtree-ldd
Version:        3.1.1
Release:        %autorelease
Summary:        Like ldd but as a tree


License:        MIT
URL:            https://github.com/haampie/libtree
Source0:        %{url}/archive/v%{version}/libtree-%{version}.tar.gz
Patch0: libtree-ldd-c99.patch

BuildRequires:  gcc
BuildRequires:  make

%description
A tool that:
- turns ldd into a tree
- explains why shared libraries are found and why not

%prep
%autosetup -p1 -n libtree-%{version}

%build
%set_build_flags
%make_build

%install
%make_install PREFIX="%{_prefix}"

%check
%ifarch i686 aarch64 s390x
# tests/05_32_bits fail after https://fedoraproject.org/wiki/Changes/glibc32_Build_Adjustments
rm -rf tests/05_32_bits
%endif
%make_build check

%files
%{_mandir}/man1/libtree.1*
%{_bindir}/libtree
%doc README.md
%license LICENSE

%changelog
%autochangelog
