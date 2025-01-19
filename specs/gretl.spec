Name: gretl	
Version: 2024d
Release: 2%{?dist}
Summary: A tool for econometric analysis

%if 0%{?fedora} >= 33
%bcond_without flexiblas
%endif

# Automatically converted from old format: GPLv3+ and BSD and MIT - review is highly recommended.
License: GPL-3.0-or-later AND LicenseRef-Callaway-BSD AND LicenseRef-Callaway-MIT
URL: http://gretl.sourceforge.net/
Source0: http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.xz
#Licensing of plugins used in gretl
Source1: gretl_plugins.txt
%if 0%{?fedora} >= 40
ExcludeArch: %{ix86}
%endif



BuildRequires:	bash-completion
%if %{with flexiblas}
BuildRequires:	flexiblas-devel
%else
BuildRequires:	blas-devel, lapack-devel
%endif
BuildRequires:	desktop-file-utils
BuildRequires:	fftw-devel
BuildRequires:	gcc-c++
BuildRequires:	gettext
BuildRequires:	glib2-devel
BuildRequires:	gmp-devel
BuildRequires:	gnuplot
BuildRequires:	gtk3-devel
BuildRequires:	gtksourceview3-devel
BuildRequires:	json-glib-devel
BuildRequires:	libcurl-devel
BuildRequires:	libxml2-devel
BuildRequires:	libgnomeui-devel
BuildRequires:	mpfr-devel
BuildRequires:	ncurses-devel
BuildRequires:	openmpi-devel
BuildRequires:	readline-devel
BuildRequires:	xdg-utils
BuildRequires:	tex(latex)
BuildRequires:	texlive-multirow

Requires: gnuplot
Requires: gtksourceview3
Requires: libcurl

%description
A cross-platform software package for econometric analysis, 
written in the C programming language.

%package devel
Summary: Development files for %{name}
Requires: %{name} = %{version}-%{release}
Requires: pkgconfig

%description devel
This package contains the development files for %{name}.

%package openmpi
Summary: Binary openmpi files for %{name}
BuildRequires: openmpi-devel
BuildRequires: make
# Require explicitly for dir ownership and to guarantee the pickup of the right runtime
Requires: openmpi
Requires: %{name} = %{version}-%{release}

%description openmpi
This package contains the binary openmpi files for %{name}.

%prep
%setup -q

CC=mpicc
CXX=mpic++
FC=mpifort

%if %{with flexiblas}
sed -i -e 's/-lblas/-lflexiblas/g' -e 's/-llapack/-lflexiblas/g' configure
%endif

%build
# Build OpenMPI version
%{_openmpi_load}
%configure	--disable-static \
		--disable-avx \
		--with-mpi \
		--with-mpi-lib=%{_libdir}/openmpi/lib/ \
		--enable-build-editor \
		--enable-build-addons \
		--enable-addons-doc \
	--with-mpi-include=%{_includedir}/openmpi-%_arch/
make %{?_smp_mflags}
cp %{SOURCE1} %{_builddir}/%{name}-%{version}/gretl_plugins.txt



%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}
%find_lang %{name}
rm -rf %{buildroot}/%{_libdir}/libgretl*.la
rm -rf %{buildroot}/%{_libdir}/gretl-gtk2/*.la
rm -rf %{buildroot}/%{_datadir}/%{name}/doc
rm -rf %{buildroot}/debug/usr/bin/*.debug

#Fix the openmpi binary
mkdir -p %{buildroot}%{_libdir}/openmpi/bin
mv %{buildroot}/%{_bindir}/gretlmpi %{buildroot}/%{_libdir}/openmpi/bin/gretl_openmpi

desktop-file-install						\
--remove-category="Application;Science;Econometrics" \
--add-category="Education;Science;Math;Economy;"  \
--dir=%{buildroot}%{_datadir}/applications     \
%{buildroot}/%{_datadir}/applications/gretl.desktop
%{_openmpi_unload}
%ldconfig_scriptlets


%files -f %{name}.lang
%{_bindir}/gretl
%{_bindir}/gretlcli
%{_bindir}/gretl_edit
%{_bindir}/gretl_x11
%{_libdir}/gretl-gtk3
%{_datadir}/%{name}/
%{_mandir}/man1/*.gz
%{_libdir}/libgretl-1.0.so.*
%{_datadir}/mime/packages/gretl.xml
%{_datadir}/icons/hicolor/32x32/apps/gretl.png
%{_datadir}/icons/hicolor/32x32/mimetypes/*.png
%{_datadir}/icons/hicolor/48x48/apps/gretl.png
%{_datadir}/icons/hicolor/64x64/apps/gretl.png
%{_datadir}/applications/gretl*
%{_datadir}/metainfo/gretl.appdata.xml

%doc ChangeLog CompatLog README gretl_plugins.txt

%files devel
%{_libdir}/pkgconfig/gretl.pc
%{_libdir}/libgretl*.so
%{_includedir}/%{name}/

%files openmpi 
%{_libdir}/openmpi/bin/gretl_openmpi

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2024d-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Dec 13 2024 Johannes Lips <hannes@fedoraproject.org> - 2024d-1
- Update to 2024d

* Tue Oct 22 2024 Johannes Lips <hannes@fedoraproject.org> - 2024c-1
- Update to 2024c

* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 2024b-3
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2024b-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue May 21 2024 Johannes Lips <hannes@fedoraproject.org> - 2024b-1
- Update to 2024b

* Sat Apr 06 2024 Johannes Lips <hannes@fedoraproject.org> - 2024a-1
- Update to 2024a

* Wed Feb 07 2024 Johannes Lips <hannes@fedoraproject.org> - 2023c-4
- enabled addons during build

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2023c-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2023c-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Dec 07 2023 Johannes Lips <hannes@fedoraproject.org> - 2023c-1
- Update to 2023c
- disable 32bit builds starting with f40

* Sun Jul 23 2023 Johannes Lips <hannes@fedoraproject.org> - 2023b-1
- Update to 2023b

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2023a-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Mar 11 2023 Johannes Lips <hannes@fedoraproject.org> - 2023a-1
- Update to 2023a

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2022c-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Nov 02 2022 Johannes Lips <hannes@fedoraproject.org> - 2022c-1
- Update to 2022c

* Wed Aug 10 2022 Johannes Lips <hannes@fedoraproject.org> - 2022b-1
- Update to 2022b
- new gretl edit binary for quick hansl development

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2022a-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Feb 02 2022 Johannes Lips <hannes@fedoraproject.org> - 2022a-1
- Update to 2022a

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2021d-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Oct 02 2021 Johannes Lips <hannes@fedoraproject.org> - 2021d-1
- Update to 2021d

* Wed Sep 01 2021 Johannes Lips <hannes@fedoraproject.org> - 2021c-1
- Update to 2021c

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2021b-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed May 05 2021 Johannes Lips <hannes@fedoraproject.org> - 2021b-1
- Update to 2021b

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2021a-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jan 18 2021 Johannes Lips <hannes@fedoraproject.org> - 2021a-1
- Update to 2021a

* Sun Nov 22 2020 Johannes Lips <hannes@fedoraproject.org> - 2020e-1
- Update to 2020e

* Thu Aug 27 2020 Iñaki Úcar <iucar@fedoraproject.org> - 2020d-2
- https://fedoraproject.org/wiki/Changes/FlexiBLAS_as_BLAS/LAPACK_manager

* Fri Aug 07 2020 Johannes Lips <hannes@fedoraproject.org> - 2020d-1
- Update to 2020d

* Fri Jul 31 2020 Johannes Lips <hannes@fedoraproject.org> - 2020c-1
- Update to 2020c

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2020b-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Apr 12 2020 Johannes Lips <hannes@fedoraproject.org> - 2020b-1
- Update to 2020b
- changelog cleanup

* Thu Mar 05 2020 Johannes Lips <hannes@fedoraproject.org> - 2020a-1
- Update to 2020a

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2019d-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Dec 23 2019 Johannes Lips <hannes@fedoraproject.org> - 2019d-1
- Update to 2019d

* Wed Oct  9 2019 Jerry James <loganjerry@gmail.com> - 2019c-3
- Rebuild for mpfr 4

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2019c-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jul 03 2019 Johannes Lips <hannes@fedoraproject.org> - 2019c-1
- Update to 2019c

* Tue May 21 2019 Johannes Lips <hannes@fedoraproject.org> - 2019b-1
- Update to 2019b

* Sun Feb 17 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2019a-4
- Rebuild for readline 8.0

* Thu Feb 14 2019 Orion Poplawski <orion@nwra.com> - 2019a-3
- Rebuild for openmpi 3.1.3

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2019a-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jan 24 2019 Johannes Lips <hannes@fedoraproject.org> - 2019a-1
- Update to 2019a

* Sat Dec 22 2018 Johannes Lips <hannes@fedoraproject.org> - 2018d-1
- Update to 2018d

* Tue Sep 04 2018 Johannes Lips <hannes@fedoraproject.org> - 2018c-1
- Update to 2018c

* Fri Aug 17 2018 Johannes Lips <hannes@fedoraproject.org> - 2018b-1
- Update to 2018b

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2018a-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Mar 17 2018 Johannes Lips <hannes@fedoraproject.org> - 2018a-1
- Update to 2018a
- removed cephes-patch

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2017d-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2017d-2
- Remove obsolete scriptlets
