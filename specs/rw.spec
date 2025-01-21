Name:		rw
Summary:	Program that calculates rank-width and rank-decompositions
Version:	0.9
Release:	9%{?dist}
License:	GPL-2.0-or-later
URL:		https://sourceforge.net/projects/rankwidth/
Source0:	https://downloads.sourceforge.net/rankwidth/%{name}-%{version}.tar.gz
# https://sourceforge.net/p/rankwidth/tickets/2/
# https://bugzilla.redhat.com//show_bug.cgi?id=2125801
# Proposal patch to support igraph 0.10
Patch0:	rw-0.9-igraph-0_10.patch
BuildRequires:	gcc
BuildRequires:	make
BuildRequires:	pkgconfig(igraph)

%description
rw is a program that calculates rank-width and rank-decompositions.
It is based on ideas from "Computing rank-width exactly" by Sang-il Oum,
"Sopra una formula numerica" by Ernesto Pascal, "Generation of a Vector
from the Lexicographical Index" by B.P. Buckles and M. Lybanon and
"Fast additions on masked integers" by Michael D. Adams and David S. Wise.

%package	devel
Summary:	Development files for %{name}
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description	devel
This package contains the header files and development documentation
for %{name}.

%prep
%autosetup

%build
%configure --disable-static

# Get rid of undesirable hardcoded rpaths; workaround libtool reordering
# -Wl,--as-needed after all the libraries.
sed -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
    -e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' \
    -e 's|CC="\(.*g..\)"|CC="\1 -Wl,--as-needed"|' \
    -i libtool

%make_build

%install
%make_install
rm %{buildroot}%{_libdir}/*.la

%files
%license COPYING
%doc %{_docdir}/%{name}/
%{_bindir}/rw
%{_libdir}/lib%{name}.so.*

%files		devel
%{_includedir}/%{name}.h
%{_libdir}/lib%{name}.so

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Dec 20 2022 Jerry James <loganjerry@gmail.com> - 0.9-4
- Convert License tag to SPDX

* Wed Sep 14 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.9-4
- Proposal patch to support igraph 0.10 (on upstream) (#2125801)

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Aug 27 2021 Jerry James <loganjerry@gmail.com> - 0.9-1
- Version 0.9
- Use sourceforge URLs

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Nov  2 2015 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 0.7-1
- Initial rw spec.
