Name:		kflickr
Version:	20100817
Release:	27%{?dist}
Summary:	Standalone Flickr Uploader

License:	GPLv2+
URL:		http://kflickr.sourceforge.net 
Source0:	http://downloads.sf.net/sourceforge/%{name}/%{name}-%{version}.tar.bz2
# man page from debian, hopefully will be adopted by new upstream
Source1:	%{name}.1

BuildRequires:	desktop-file-utils, gettext, cmake
BuildRequires:	kdelibs4-devel
BuildRequires: make
Requires:	kdebase-runtime%{?_kde4_version: >= %{_kde4_version}}

%{?_kde4_macros_api:Requires: kde4-macros(api) = %{_kde4_macros_api} } 

%description
kflickr is an easy to use photo uploader for flickr.

%prep
%setup -q

# Make desktop file UTF compat
for file in desktop/kflickr.desktop ; do
  iconv -f ISO-8859-5 -t UTF-8 $file > $file.tmp && \
    mv $file.tmp $file || rm -f $file.tmp
done

# update desktop file
sed -i 's#Categories=KDE;#Categories=KDE;Qt;#g' desktop/kflickr.desktop
%build

%{cmake_kde4} .
make %{?_smp_mflags}


%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}

# Desktop file
desktop-file-install \
--dir %{buildroot}%{_datadir}/applications/ \
--vendor="" \
desktop/kflickr.desktop

# HTML
HTML_DIR=$(kde4-config --expandvars --install html)
# install docs
cd doc
for i in *; do 
mkdir -p %{buildroot}$HTML_DIR/$i/%{name}
cp -pR $i/* %{buildroot}$HTML_DIR/$i/%{name}/
pushd %{buildroot}/$HTML_DIR/$i/%{name}
ln -s ../../$i/common common
popd
done
cd ..
%find_lang %{name} --with-kde
# install man page
mkdir -p %{buildroot}%{_mandir}/man1/
install -pm 0644 %{SOURCE1} %{buildroot}%{_mandir}/man1/

%files  -f %{name}.lang
%doc AUTHORS COPYING COPYING-DOCS README 
%{_bindir}/*
%{_datadir}/icons/hicolor/*/apps/*
%{_datadir}/applications/kde4/*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/kde4/apps/*
%{_mandir}/man1/*

%changelog
* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 20100817-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 20100817-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 20100817-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 20100817-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 20100817-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20100817-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20100817-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20100817-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20100817-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20100817-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20100817-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 20100817-16
- Remove obsolete scriptlets

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20100817-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20100817-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20100817-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 20100817-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20100817-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 20100817-10
- Rebuilt for GCC 5 C++11 ABI change

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20100817-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20100817-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20100817-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20100817-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20100817-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20100817-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat Jul 23 2011 Jan Klepek <jan.klepek at, gmail.com> - 20100817-3
- Updated Requires and fixed icon handling

* Mon Mar 21 2011 Jan Klepek <jan.klepek at, gmail.com> - 20100817-2
- updated Buildrequires and requires

* Sun Mar 13 2011 Jan Klepek <jan.klepek at, gmail.com> - 20100817-1
- updated to latest version and rewritten spec file

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Dec  4 2008 Michael Schwendt <mschwendt@fedoraproject.org> - 0.9.1-3
- Include unowned directories.

* Tue Apr 01 2008 Rex Dieter <rdieter@fedoraproject.org> - 0.9.1-2
- fix rawhide build (#434440)
- s/kdebase3-devel/kdelibs3-devel/
- fix SOURCE url

* Sat Feb 23 2008 Michael Stahnke <mastahnke@gmail.com> - 0.9.1-1
- New upstream

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.9-2
- Autorebuild for GCC 4.3

* Tue Sep 18 2007 Michael Stahnke <mastahnke@gmail.com> - 0.9-1
- License updated per new guidelines 
- Bump for upstream release (0.9)

* Mon May 14 2007 Michael Stahnke <mastahnke@gmail.com> - 0.8-3
- Final touch-up for review bug # 237355

* Mon May 14 2007 Michael Stahnke <mastahnke@gmail.com> - 0.8-2
- Minor fix for bug # 237355

* Thu Apr 19 2006 Michael Stahnke <mastahnke@gmail.com> - 0.8-1
- Initial Package
