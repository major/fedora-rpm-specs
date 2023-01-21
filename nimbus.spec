# Define Variables that must exist
%{?!rhel:%define rhel 0}
%{?!fedora:%define fedora 0}

Name:           nimbus
Version:        0.1.4
Release:        26%{?dist}
Summary:        Desktop theme originally from Sun

License:        LGPLv2
URL:            https://nimbus.dev.java.net/
Source0:        http://dlc.sun.com/osol/jds/downloads/extras/nimbus/nimbus-%{version}.tar.bz2
Patch0:         nimbus-0.1.4-stock-icons.patch

BuildRequires: make
BuildRequires:  gcc
BuildRequires:  icon-naming-utils glib2-devel gtk2-devel gettext intltool

%description
Virtual package to collect all Nimbus related components.

%package -n     nimbus-theme-gnome
Summary:        Desktop theme from Sun
Requires:       gtk-nimbus-engine, nimbus-icon-theme, nimbus-metacity-theme
%if 0%{?fedora} >= 10
BuildArch:      noarch
%endif


%description -n nimbus-theme-gnome
The Nimbus theme pack for Gnome make use of Nimbus Metacity theme, Nimbus
GTK2 theme and icon set. It originates from OpenSolaris by Sun.


%package -n     gtk-nimbus-engine
Summary:        Gtk+ engine for %{name}
Requires:       gtk2-engines

%description -n gtk-nimbus-engine
GTK+ engine for %{name}.


%package -n     nimbus-icon-theme
Summary:        Icons for %{name}
%if 0%{?fedora} >= 10
BuildArch:      noarch
%endif
%if 0%{?fedora}
Requires:       fedora-logos
%endif
%if 0%{?rhel}
Requires:       redhat-artwork
%endif

%description -n nimbus-icon-theme
Icons for %{name}.


%package -n     nimbus-metacity-theme
Summary:        Metacity theme for %{name}
%if 0%{?fedora} >= 10
BuildArch:      noarch
%endif
Requires:       metacity

%description -n nimbus-metacity-theme
Theme for metacity as part of %{name}.


%prep
%setup -q -n nimbus-%{version}
%patch0 -p1 -b .stock-icons

# convert to utf-8
iconv --from=ISO-8859-1 --to=UTF-8 ChangeLog > ChangeLog.new && \
touch -r ChangeLog ChangeLog.new && \
mv ChangeLog.new ChangeLog


%build
%configure --disable-static
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
# remove libtool archives
find $RPM_BUILD_ROOT%{_libdir}/gtk-2.0/ \( -name \*.la -o -name \*.a \) -delete
install -Dp -m 0644 index.theme \
	 $RPM_BUILD_ROOT%{_datadir}/themes/nimbus/index.theme
touch $RPM_BUILD_ROOT%{_datadir}/icons/nimbus/icon-theme.cache

# installed due to error in Makefile
rm -f $RPM_BUILD_ROOT%{_datadir}/themes/nimbus/dark-index.theme
rm -f $RPM_BUILD_ROOT%{_datadir}/themes/nimbus/light-index.theme

# removing OpenSolaris branding use vendor's start-here.png
%if 0%{?fedora}
%define theme_name Fedora
%else
%define theme_name Bluecurve
%endif
find $RPM_BUILD_ROOT%{_datadir}/icons/nimbus/ -name start-here.png \
	|while read FILENAME ; do
		NEWICON=$(echo $FILENAME \
		|sed -e "s!$RPM_BUILD_ROOT.*nimbus\(.*\)\$!\.\./\.\./\.\./%{theme_name}\1!")
%if 0%{?rhel}
		NEWICON=$(echo $NEWICON|sed -e 's/places/mimetypes/')
%endif
		ln -sf -v $NEWICON $FILENAME
	done
	


%post -n nimbus-icon-theme
touch --no-create %{_datadir}/icons/nimbus &>/dev/null || :


%postun -n nimbus-icon-theme
if [ $1 -eq 0 ] ; then
	 touch --no-create %{_datadir}/icons/nimbus &>/dev/null
	 gtk-update-icon-cache %{_datadir}/icons/nimbus &>/dev/null || :
fi


%posttrans -n nimbus-icon-theme
gtk-update-icon-cache %{_datadir}/icons/nimbus &>/dev/null || :


%files -n gtk-nimbus-engine
%doc AUTHORS ChangeLog COPYING gtk-engine/docs.txt
%{_libdir}/gtk-2.0/*/engines/libnimbus.so
%dir %{_datadir}/themes/nimbus/
%dir %{_datadir}/themes/nimbus/gtk-2.0/
%{_datadir}/themes/nimbus/gtk-2.0/gtkrc
%dir %{_datadir}/themes/dark-nimbus/
%dir %{_datadir}/themes/dark-nimbus/gtk-2.0/
%{_datadir}/themes/dark-nimbus/gtk-2.0/gtkrc
%dir %{_datadir}/themes/light-nimbus/
%dir %{_datadir}/themes/light-nimbus/gtk-2.0/
%{_datadir}/themes/light-nimbus/gtk-2.0/gtkrc


%files -n nimbus-metacity-theme
%doc AUTHORS ChangeLog COPYING
%dir %{_datadir}/themes/nimbus/
%{_datadir}/themes/nimbus/metacity-1/
%dir %{_datadir}/themes/dark-nimbus/
%{_datadir}/themes/dark-nimbus/metacity-1/
%dir %{_datadir}/themes/light-nimbus/
%{_datadir}/themes/light-nimbus/metacity-1/


%files -n nimbus-icon-theme
%doc AUTHORS ChangeLog COPYING
%dir %{_datadir}/icons/nimbus/
%{_datadir}/icons/nimbus/*x*
%{_datadir}/icons/nimbus/iconrc
%ghost %{_datadir}/icons/nimbus/icon-theme.cache


%files -n nimbus-theme-gnome
%{_datadir}/themes/nimbus/index.theme
%{_datadir}/themes/dark-nimbus/index.theme
%{_datadir}/themes/light-nimbus/index.theme

%changelog
* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.4-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.4-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.4-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.4-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.4-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.4-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.4-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.4-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.4-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.4-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.4-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.4-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.4-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.4-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.4-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 0.1.4-4
- Rebuild for new libpng

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Nov 22 2009 Christoph Wickert <cwickert@fedoraproject.org> - 0.1.4-2
- Fix srciptlets of nimbus-icon-theme

* Sun Nov 22 2009 Christoph Wickert <cwickert@fedoraproject.org> - 0.1.4-1
- Update to 0.1.4

* Fri Nov 13 2009 Christoph Wickert <cwickert@fedoraproject.org> - 0.0.17-8.1
- Remove reference to non existant notification engine (#537161)

* Wed Sep  9 2009 Matěj Cepl <mcepl@redhat.com> - 0.0.17-8
- use %%if and build both on RHEL and Fedora.

* Wed Aug  5 2009 Matěj Cepl <mcepl@redhat.com> - 0.0.17-6
- remove OpenSolaris branding
- add Requires for fedora-logos to nimbus-icon-theme

* Tue Aug  4 2009 Matěj Cepl <mcepl@redhat.com> - 0.0.17-5
- new version of nimbus-0.0.17-stock-icons.patch
- remove another unnecessary %%dir in %%files

* Sat May 16 2009 matej <mcepl@redhat.com> 0.0.17-4
- reogrganization of subpackages
- many changes in %%files

* Mon Apr 20 2009 Matej Cepl <mcepl@redhat.com> 0.0.17-3
- Packaging Review fixes

* Thu Mar 12 2009 Matej Cepl <mcepl@redhat.com> 0.0.17-2
- Fix License tag.

* Mon Mar 02 2009 Matej Cepl <mcepl@redhat.com> 0.0.17-1
- Initial affert to package
