%global extdir     %{_datadir}/gnome-shell/extensions/pidgin@muffinmad
%global gschemadir %{_datadir}/glib-2.0/schemas
%global gitname    pidgin-im-gnome-shell-extension
%global giturl     https://github.com/muffinmad/%{gitname}


Name:		gnome-shell-extension-pidgin
Version:	47
Release:	3%{?dist}
Summary:	Make Pidgin IM conversations appear in the Gnome Shell message tray

License:	GPL-2.0-or-later
URL:		https://extensions.gnome.org/extension/782/pidgin-im-integration/
Source0:	%{giturl}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildArch:	noarch

BuildRequires:	gettext

Requires:	gnome-shell-extension-common

%description
This package contains the necessary components to integrate pidgin with 
GNOME Shell.


%prep
%autosetup -n %{gitname}-%{version}

# It works in 46 too, which is what rawhide has (2024-02-10)
sed -i 's|"45"|"45", "46"|g' metadata.json

%build
# Remove useless files.
%{_bindir}/find . -name '*.po' -print -delete
%{_bindir}/find . -name '*.pot' -print -delete


%install
# Create needed dirs.
%{__mkdir} -p %{buildroot}%{extdir} %{buildroot}%{gschemadir}

# Install everything to its proper location.
%{__cp} -pr . %{buildroot}%{extdir}
%{__cp} -pr ./locale %{buildroot}%{_datadir}
%{__cp} -pr ./schemas/*gschema.xml %{buildroot}%{gschemadir}

# Remove unneded files.
%{__rm} -fr %{buildroot}%{extdir}/{LICENSE,README*,locale,schemas}

# Create manifest for i18n.
%find_lang %{name} --all-name


# Fedora handles this using triggers.
%if 0%{?rhel} && 0%{?rhel} <= 7
%postun
if [ $1 -eq 0 ] ; then
        %{_bindir}/glib-compile-schemas %{gschemadir} &> /dev/null || :
fi


%posttrans
%{_bindir}/glib-compile-schemas %{gschemadir} &> /dev/null || :
%endif


%files -f %{name}.lang
%license LICENSE
%doc README.md
%{extdir}
%{gschemadir}/*gschema.xml


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 47-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 47-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Feb 10 2024 Tom Callaway <spot@fedoraproject.org> - 47-1
- update to 47

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Dec 02 2017 Björn Esser <besser82@fedoraproject.org> - 1.0.3-1
- New upstream release
- Build noarch'ed, no need for a native extension anymore
- Use upstreams versioning scheme
- Simplify packaging

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.23.gitfb9dbfd
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.22.gitfb9dbfd
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.21.gitfb9dbfd
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.20.gitfb9dbfd
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.19.gitfb9dbfd
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Mar 27 2015 Tom Callaway <spot@fedoraproject.org> - 0-0.18.gitfb9dbfd
- update to latest git
- enable support for gnome 3.15/3.16

* Wed Feb 25 2015 Ville Skyttä <ville.skytta@iki.fi> - 0-0.17.gitf1beeeb
- Switch to github provided tarball, don't ship .git or *.po
- Mark license files as %%license

* Tue Jan 20 2015 Tom Callaway <spot@fedoraproject.org> - 0-0.16.git1a254319ea
- switch to pidgin-im-gnome-shell-extension@muffinmad

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.15.git1a254319ea
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.14.git1a254319ea
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Mar 24 2014 Tom Callaway <spot@fedoraproject.org> - 0-0.13.git1a254319ea
- conf fixes

* Mon Feb  3 2014 Tom Callaway <spot@fedoraproject.org> - 0-0.12.git1a254319ea
- fix zombie notifications (they would not die, now they do)

* Wed Oct 23 2013 Tom Callaway <spot@fedoraproject.org> - 0-0.11.git1a254319ea
- update to Psykar fork of extension (works with 3.8 and 3.10)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.10.git87fc23433d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb  8 2013 Tom Callaway <spot@fedoraproject.org> - 0-0.9.git87fc23433d
- apply fixes from "thedeadparrot" github fork to get things working on gnome 3.6
- improve gnome-shell connector plugin

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.8.git87fc23433d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Apr  5 2012 Tom Callaway <spot@fedoraproject.org> - 0-0.7.git87fc23433d
- sync with git
- tell extension it is okay for gnome-shell 3.4

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.6.git80d4ea4b59
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Oct  7 2011 Tom Callaway <spot@fedoraproject.org> - 0-0.5.git80d4ea4b59
- update to the latest code with more proper 3.2 fixes

* Sun Oct  2 2011 Tom Callaway <spot@fedoraproject.org> - 0-0.4.git4ca78b1
- fix metadata version to be 3.2

* Fri Sep 23 2011 Tom Callaway <spot@fedoraproject.org> - 0-0.3.git4ca78b1
- gnome 3.2 fix

* Wed Jun 15 2011 Tom Callaway <spot@fedoraproject.org> - 0-0.2.git4ca78b1
- add gpl-2.0.txt and license explanation as docs

* Mon Jun 06 2011 Tom Callaway <spot@fedoraproject.org> - 0-0.1.git4ca78b1
- Initial package for Fedora
