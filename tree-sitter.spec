%global treesitter_so_version 0

Name:           tree-sitter
Version:        0.22.2
Release:        1%{?dist}
Summary:        An incremental parsing system for programming tools

License:        MIT
URL:            https://tree-sitter.github.io/
Source0:        https://github.com/tree-sitter/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires: gcc
BuildRequires: make


%description
Tree-sitter is a parser generator tool and an incremental parsing
library. It can build a concrete syntax tree for a source file
and efficiently update the syntax tree as the source file is
edited. Tree-sitter aims to be:

 * General enough to parse any programming language
 * Fast enough to parse on every keystroke in a text editor
 * Robust enough to provide useful results even in the presence
   of syntax errors
 * Dependency-free so that the runtime library (which is written
   in pure C) can be embedded in any application

%package -n lib%{name}
Summary:        Incremental parsing library for programming tools

%description -n lib%{name}
Tree-sitter is a parser generator tool and an incremental parsing
library. It can build a concrete syntax tree for a source file
and efficiently update the syntax tree as the source file is
edited. This is the package with the dynamically linked C library.

%package -n lib%{name}-devel
Summary:        Development files for %{name}
Requires:       lib%{name}%{?_isa} = %{version}-%{release}

%description -n lib%{name}-devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -p1


%build
%set_build_flags
export PREFIX='%{_prefix}' LIBDIR='%{_libdir}'
%make_build


%install
export PREFIX='%{_prefix}' LIBDIR='%{_libdir}' INCLUDEDIR='%{_includedir}'
%make_install

find %{buildroot}%{_libdir} -type f \( -name "*.la" -o -name "*.a" \) -delete -print


%files -n lib%{name}
%license LICENSE
%doc README.md CHANGELOG.md
%{_libdir}/libtree-sitter.so.%{treesitter_so_version}*

%files -n lib%{name}-devel
%{_includedir}/tree_sitter
%{_libdir}/libtree-sitter.so
%{_libdir}/pkgconfig/tree-sitter.pc


%changelog
* Mon Mar 18 2024 Andreas Schneider <asn@redhat.com> - 0.22.2-1
- Update to version 0.22.2
  https://github.com/tree-sitter/tree-sitter/blob/v0.22.2/CHANGELOG.md

* Mon Mar 11 2024 Andreas Schneider <asn@redhat.com> - 0.22.1-1
- Update to version 0.22.1
  https://github.com/tree-sitter/tree-sitter/blob/v0.22.1/CHANGELOG.md

* Thu Feb 22 2024 Andreas Schneider <asn@redhat.com> - 0.21.0-1
- Update to version 0.21.0
  https://github.com/tree-sitter/tree-sitter/releases/tag/v0.21.0

* Fri Jan 26 2024 Andreas Schneider <asn@redhat.com> - 0.20.9-1
- Update to version 0.20.9
  https://github.com/tree-sitter/tree-sitter/releases/tag/v0.20.9

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.20.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Apr 04 2023 Andreas Schneider <asn@redhat.com> - 0.20.8-1
- Update to version 0.20.8

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.20.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Sep 03 2022 Andreas Schneider <asn@redhat.com> - 0.20.7-1
- Update to version 0.20.7

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.20.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Apr 04 2022 Andreas Schneider <asn@redhat.com> - 0.20.6-1
- Update to version 0.20.6

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.20.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Dec 01 2021 Andreas Schneider <asn@redhat.com> - 0.20.1-1
- Update to version 0.20.1

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.20.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat Jul 03 2021 Andreas Schneider <asn@redhat.com> - 0.20.0-2
- Fixed libtree-sitter Require of devel package

* Fri Jul 02 2021 Andreas Schneider <asn@redhat.com> - 0.20.0-1
- Initial package
