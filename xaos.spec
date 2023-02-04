Name:           xaos
Version:        3.6
Release:        20%{?dist}
Summary:        A fast, portable real-time interactive fractal zoomer

License:        GPLv2+
URL:            http://xaos.sourceforge.net
Source0:        http://surfnet.dl.sourceforge.net/sourceforge/xaos/xaos-%{version}.tar.gz
Source1:	xaos.png
Patch0:	xaos-3.6-fix-conflicting-register-types.patch
Patch1:	xaos-3.6-format-security.patch
Patch2: xaos-c99.patch
BuildRequires: make
BuildRequires:  gcc
BuildRequires:  slang-devel
BuildRequires:	zlib-devel
BuildRequires:	libpng-devel
BuildRequires:	aalib-devel
BuildRequires:  gpm-devel
BuildRequires:  gsl-devel
BuildRequires:  gtk2-devel
BuildRequires:	ncurses-devel
BuildRequires:	libXt-devel
BuildRequires:	libX11-devel
BuildRequires:	libXext-devel
BuildRequires:	libXxf86vm-devel
BuildRequires:	libXxf86dga-devel
BuildRequires:	dvipdfm
BuildRequires:	texinfo
BuildRequires:	texinfo-tex
BuildRequires:  desktop-file-utils
BuildRequires:	gettext


%description
XaoS is a fast, portable real-time interactive fractal zoomer. It
displays the Mandelbrot set (among other escape time fractals) and
allows you zoom smoothly into the fractal. Various coloring modes are
provided for both the points inside and outside the selected set. XaoS
supports switching between Julia and Mandelbrot fractal types and
on-the-fly plane switching.


%prep
%setup0 -q 
%patch0 -p1 -b .proto
%patch1 -p1 -b .formatsec
%patch2 -p1
# disable stripping binaries when installing
sed -i 's| -s | |' Makefile.in

%build
%ifarch %ix86 x86_64
%define long_double --with-long-double
%endif
%configure \
    --with-gsl=yes \
    --with-sffe=yes \
    --with-png=yes \
    --with-gtk-driver=yes \
    --with-aa-driver=yes \
    --with-pthread=yes \
    %{long_double}
make %{?_smp_mflags}


%install
mkdir -p $RPM_BUILD_ROOT%{_infodir}
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"
pushd doc
make xaos.dvi
dvipdfm xaos.dvi
popd
pushd help
make html
popd

# Setup the doc dir structure for install via %%doc
mv help help-build
mkdir help
cp -pr help-build/*.html help/
cp -pr help-build/*.css help/
cp -pr help-build/*.jpg help/

mkdir -p $RPM_BUILD_ROOT%{_datadir}/pixmaps
cp -p %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/pixmaps

cat > xaos.desktop <<EOF
[Desktop Entry]
Name=XaoS
Comment=Interactive fractal zoomer
Exec=xaos -driver "GTK+ Driver"
Icon=xaos
Terminal=false
Type=Application
Categories=Application;Education;Math;Graphics;
Encoding=UTF-8
X-Desktop-File-Install-Version=0.10
EOF

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
desktop-file-install \
        --dir $RPM_BUILD_ROOT%{_datadir}/applications \
        xaos.desktop

rm -f $RPM_BUILD_ROOT%{_datadir}/XaoS/catalogs/README
rm -fr $RPM_BUILD_ROOT%{_datadir}/XaoS/doc
rm -f $RPM_BUILD_ROOT%{_infodir}/dir

find $RPM_BUILD_ROOT%{_prefix} -exec chmod u+rw '{}' ';'

%find_lang %{name}

%files -f %{name}.lang
%doc README COPYING TODO ChangeLog NEWS
%doc AUTHORS doc/xaos.pdf
%doc help
%{_bindir}/*
%{_infodir}/*
%{_datadir}/XaoS
%{_datadir}/applications/*
%{_datadir}/pixmaps/*
%{_mandir}/man*/*


%changelog
* Thu Feb 02 2023 Florian Weimer <fweimer@redhat.com> - 3.6-20
- Fix C99 compatibility issues

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.6-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Aug 23 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.6-18
- Rebuild for gsl-2.7.1

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.6-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.6-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.6-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.6-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.6-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.6-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Aug 20 2019 Susi Lehtola <jussilehtola@fedoraproject.org> - 3.6-11
- Rebuilt for GSL 2.6.

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.6-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Feb 22 2016 Orion Poplawski <orion@cora.nwra.com> - 3.6-3
- Rebuild for gsl 2.1

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jul  9 2015 Gérard Milmeister <gemi@bluewin.ch> - 3.6-1
- new release 3.6

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.5-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.5-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Wed Jun 25 2014 Yaakov Selkowitz <yselkowi@redhat.com> - 3.5-11
- Fix FTBFS with -Werror=format-security (#1037389, #1107203)

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Toshio Kuratomi <toshio@fedoraproject.org> - 3.5-8
- Rework help doc installation so that it will build with F19's rpm

* Sun Feb 10 2013 Parag Nemade <paragn AT fedoraproject DOT org> - 3.5-7
- Remove vendor tag from desktop file as per https://fedorahosted.org/fesco/ticket/1077
- Cleanup spec as per recently changed packaging guidelines

* Wed Aug  1 2012 Mamoru Tasaka <mtasaka@fedoraproject.org> - 3.5-6
- Fix gcc build error wrt conflicting types for register attribute

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 3.5-3
- Rebuild for new libpng

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jul 25 2009 Gerard Milmeister <gemi@bluewin.ch> - 3.5-1
- new release 3.5
- Enable long double on ix86 and x86_64 architectures.
- Enable i386 inline assembly on ix86.
- Enable threads on all architectures

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Aug 20 2008 Gerard Milmeister <gemi@bluewin.ch> - 3.4-2
- enabled GTK driver

* Wed Aug 20 2008 Gerard Milmeister <gemi@bluewin.ch> - 3.4-1
- new release 3.4

* Tue Aug 12 2008 Jason L Tibbitts III <tibbs@math.uh.edu> - 3.2.3-5
- Fix license tag.

* Fri Feb 22 2008 Gerard Milmeister <gemi@bluewin.ch> - 3.2.3-3
- added BR dvipdfm

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 3.2.3-2
- Autorebuild for GCC 4.3

* Sat Dec  2 2006 Gerard Milmeister <gemi@bluewin.ch> - 3.2.3-1
- new version 3.2.3

* Sun Nov  5 2006 Gerard Milmeister <gemi@bluewin.ch> - 3.2.2-1
- new version 3.2.2

* Mon Aug 28 2006 Gerard Milmeister <gemi@bluewin.ch> - 3.2.1-4
- Rebuild for FE6
- added BR: gettext

* Sat Jun 10 2006 Gerard Milmeister <gemi@bluewin.ch> - 3.2.1-3
- disabled stripping of binaries

* Tue Jun  6 2006 Gerard Milmeister <gemi@bluewin.ch> - 3.2.1-2
- added BuildReq: libXt-devel
- fixed permissions
- added .desktop file
- added icon

* Sun Jun  4 2006 Gerard Milmeister <gemi@bluewin.ch> - 3.2.1-1
- new version 3.2.1

* Sat Feb  4 2006 Gerard Milmeister <gemi@bluewin.ch> - 3.2-1
- new version 3.2

* Sun Dec 18 2005 Gerard Milmeister <gemi@bluewin.ch> - 3.1.3-1
- New Version 3.1.3

* Thu Mar 31 2005 Gerard Milmeister <gemi@bluewin.ch> - 0:3.1-0.fdr.1
- New Version 3.1.2

* Sun Jul 18 2004 Gerard Milmeister <gemi@bluewin.ch> - 0:3.1-0.fdr.1
- First Fedora release
