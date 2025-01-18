%global vergit  20220304
%global tname   Flat-Remix

Name:           flat-remix-icon-theme
Version:        0.0.%{vergit}
Release:        9%{?dist}
Summary:        Icon theme inspired on material design

# The entire source code is GPLv3+ except:
# GPLv3:        Numix icon theme
#               Papirus icon theme
# CC-BY-SA:     EvoPop icon theme
#               Flattr icon theme
#               Paper icon theme
# Automatically converted from old format: GPLv3+ and CC-BY-SA - review is highly recommended.
License:        GPL-3.0-or-later AND LicenseRef-Callaway-CC-BY-SA
URL:            https://github.com/daniruiz/flat-remix
Source0:        %{url}/archive/%{vergit}/%{name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  make

Requires:       adwaita-icon-theme
Requires:       gnome-icon-theme
Requires:       hicolor-icon-theme

Recommends:     flat-remix-gtk2-theme
Recommends:     flat-remix-gtk3-theme

Suggests:       flat-remix-theme
Suggests:       gnome-shell-theme-flat-remix

%description
Flat Remix icon theme is a pretty simple Linux icon theme inspired on material
design. It is mostly flat with some shadows, highlights and gradients for some
depth, and uses a colorful palette with nice contrasts.


%prep
%autosetup -n flat-remix-%{vergit}


%build
%make_build


%install
%make_install

export THEMES="Flat-Remix-Black-Dark Flat-Remix-Black-Light Flat-Remix-Black-Light-darkPanel Flat-Remix-Blue-Dark Flat-Remix-Blue-Light Flat-Remix-Blue-Light-darkPanel Flat-Remix-Brown-Dark Flat-Remix-Brown-Light Flat-Remix-Brown-Light-darkPanel Flat-Remix-Cyan-Dark Flat-Remix-Cyan-Light Flat-Remix-Cyan-Light-darkPanel Flat-Remix-Green-Dark Flat-Remix-Green-Light Flat-Remix-Green-Light-darkPanel Flat-Remix-Grey-Dark Flat-Remix-Grey-Light Flat-Remix-Grey-Light-darkPanel Flat-Remix-Magenta-Dark Flat-Remix-Magenta-Light Flat-Remix-Magenta-Light-darkPanel Flat-Remix-Orange-Dark Flat-Remix-Orange-Light Flat-Remix-Orange-Light-darkPanel Flat-Remix-Red-Dark Flat-Remix-Red-Light Flat-Remix-Red-Light-darkPanel Flat-Remix-Teal-Dark Flat-Remix-Teal-Light Flat-Remix-Teal-Light-darkPanel Flat-Remix-Violet-Dark Flat-Remix-Violet-Light Flat-Remix-Violet-Light-darkPanel Flat-Remix-Yellow-Dark Flat-Remix-Yellow-Light Flat-Remix-Yellow-Light-darkPanel"
for t in $THEMES; do
    /bin/touch %{buildroot}/%{_datadir}/icons/$t/icon-theme.cache
done


# Workaround for replace directory with symlink which was added in "20211214"
# version
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Directory_Replacement/#_scriptlet_to_replace_a_directory
%pretrans -p <lua>
path = "%{_datadir}/icons/Flat-Remix-Blue-Light"
st = posix.stat(path)
if st and st.type == "directory" then
  status = os.rename(path, path .. ".rpmmoved")
  if not status then
    suffix = 0
    while not status do
      suffix = suffix + 1
      status = os.rename(path .. ".rpmmoved", path .. ".rpmmoved." .. suffix)
    end
    os.rename(path, path .. ".rpmmoved")
  end
end

path = "%{_datadir}/icons/Flat-Remix-Green-Light"
st = posix.stat(path)
if st and st.type == "directory" then
  status = os.rename(path, path .. ".rpmmoved")
  if not status then
    suffix = 0
    while not status do
      suffix = suffix + 1
      status = os.rename(path .. ".rpmmoved", path .. ".rpmmoved." .. suffix)
    end
    os.rename(path, path .. ".rpmmoved")
  end
end

path = "%{_datadir}/icons/Flat-Remix-Red-Light"
st = posix.stat(path)
if st and st.type == "directory" then
  status = os.rename(path, path .. ".rpmmoved")
  if not status then
    suffix = 0
    while not status do
      suffix = suffix + 1
      status = os.rename(path .. ".rpmmoved", path .. ".rpmmoved." .. suffix)
    end
    os.rename(path, path .. ".rpmmoved")
  end
end

path = "%{_datadir}/icons/Flat-Remix-Yellow-Light"
st = posix.stat(path)
if st and st.type == "directory" then
  status = os.rename(path, path .. ".rpmmoved")
  if not status then
    suffix = 0
    while not status do
      suffix = suffix + 1
      status = os.rename(path .. ".rpmmoved", path .. ".rpmmoved." .. suffix)
    end
    os.rename(path, path .. ".rpmmoved")
  end
end


%post
export THEMES="Flat-Remix-Black-Dark Flat-Remix-Black-Light Flat-Remix-Black-Light-darkPanel Flat-Remix-Blue-Dark Flat-Remix-Blue-Light Flat-Remix-Blue-Light-darkPanel Flat-Remix-Brown-Dark Flat-Remix-Brown-Light Flat-Remix-Brown-Light-darkPanel Flat-Remix-Cyan-Dark Flat-Remix-Cyan-Light Flat-Remix-Cyan-Light-darkPanel Flat-Remix-Green-Dark Flat-Remix-Green-Light Flat-Remix-Green-Light-darkPanel Flat-Remix-Grey-Dark Flat-Remix-Grey-Light Flat-Remix-Grey-Light-darkPanel Flat-Remix-Magenta-Dark Flat-Remix-Magenta-Light Flat-Remix-Magenta-Light-darkPanel Flat-Remix-Orange-Dark Flat-Remix-Orange-Light Flat-Remix-Orange-Light-darkPanel Flat-Remix-Red-Dark Flat-Remix-Red-Light Flat-Remix-Red-Light-darkPanel Flat-Remix-Teal-Dark Flat-Remix-Teal-Light Flat-Remix-Teal-Light-darkPanel Flat-Remix-Violet-Dark Flat-Remix-Violet-Light Flat-Remix-Violet-Light-darkPanel Flat-Remix-Yellow-Dark Flat-Remix-Yellow-Light Flat-Remix-Yellow-Light-darkPanel"
for t in $THEMES; do
    /bin/touch --no-create %{_datadir}/icons/$t &>/dev/null || :
done

%postun
if [ $1 -eq 0 ] ; then
    export THEMES="Flat-Remix-Black-Dark Flat-Remix-Black-Light Flat-Remix-Black-Light-darkPanel Flat-Remix-Blue-Dark Flat-Remix-Blue-Light Flat-Remix-Blue-Light-darkPanel Flat-Remix-Brown-Dark Flat-Remix-Brown-Light Flat-Remix-Brown-Light-darkPanel Flat-Remix-Cyan-Dark Flat-Remix-Cyan-Light Flat-Remix-Cyan-Light-darkPanel Flat-Remix-Green-Dark Flat-Remix-Green-Light Flat-Remix-Green-Light-darkPanel Flat-Remix-Grey-Dark Flat-Remix-Grey-Light Flat-Remix-Grey-Light-darkPanel Flat-Remix-Magenta-Dark Flat-Remix-Magenta-Light Flat-Remix-Magenta-Light-darkPanel Flat-Remix-Orange-Dark Flat-Remix-Orange-Light Flat-Remix-Orange-Light-darkPanel Flat-Remix-Red-Dark Flat-Remix-Red-Light Flat-Remix-Red-Light-darkPanel Flat-Remix-Teal-Dark Flat-Remix-Teal-Light Flat-Remix-Teal-Light-darkPanel Flat-Remix-Violet-Dark Flat-Remix-Violet-Light Flat-Remix-Violet-Light-darkPanel Flat-Remix-Yellow-Dark Flat-Remix-Yellow-Light Flat-Remix-Yellow-Light-darkPanel"
    for t in $THEMES; do
        /bin/touch --no-create %{_datadir}/icons/$t &>/dev/null
        /usr/bin/gtk-update-icon-cache %{_datadir}/icons/$t &>/dev/null || :
    done
fi

%posttrans
export THEMES="Flat-Remix-Black-Dark Flat-Remix-Black-Light Flat-Remix-Black-Light-darkPanel Flat-Remix-Blue-Dark Flat-Remix-Blue-Light Flat-Remix-Blue-Light-darkPanel Flat-Remix-Brown-Dark Flat-Remix-Brown-Light Flat-Remix-Brown-Light-darkPanel Flat-Remix-Cyan-Dark Flat-Remix-Cyan-Light Flat-Remix-Cyan-Light-darkPanel Flat-Remix-Green-Dark Flat-Remix-Green-Light Flat-Remix-Green-Light-darkPanel Flat-Remix-Grey-Dark Flat-Remix-Grey-Light Flat-Remix-Grey-Light-darkPanel Flat-Remix-Magenta-Dark Flat-Remix-Magenta-Light Flat-Remix-Magenta-Light-darkPanel Flat-Remix-Orange-Dark Flat-Remix-Orange-Light Flat-Remix-Orange-Light-darkPanel Flat-Remix-Red-Dark Flat-Remix-Red-Light Flat-Remix-Red-Light-darkPanel Flat-Remix-Teal-Dark Flat-Remix-Teal-Light Flat-Remix-Teal-Light-darkPanel Flat-Remix-Violet-Dark Flat-Remix-Violet-Light Flat-Remix-Violet-Light-darkPanel Flat-Remix-Yellow-Dark Flat-Remix-Yellow-Light Flat-Remix-Yellow-Light-darkPanel"
for t in $THEMES; do
    /usr/bin/gtk-update-icon-cache %{_datadir}/icons/$t &>/dev/null || :
done


%files
%license LICENSE
%doc README.md AUTHORS CHANGELOG
%dir %{_datadir}/icons/%{tname}-*/
%{_datadir}/icons/%{tname}-*/{actions/,animations/,apps/,categories/,devices/,emblems/,emotes/,mimetypes/,panel/,places/,status/,index.theme}
%ghost %{_datadir}/icons/%{tname}-{Blue,Green,Red,Yellow}-Light.rpmmoved/
%ghost %{_datadir}/icons/%{tname}-*/icon-theme.cache


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.20220304-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Aug 28 2024 Miroslav Suchý <msuchy@redhat.com> - 0.0.20220304-8
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.20220304-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.20220304-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.20220304-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.20220304-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.20220304-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.20220304-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Apr 16 2022 Artem Polishchuk <ego.cordatus@gmail.com> - 0.0.20220304-1
- Update to 20220304

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.20211214-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sun Jan 02 2022 Artem Polishchuk <ego.cordatus@gmail.com> - 0.0.20211214-2
- build: Workaround for replace directory with symlink which was added in
  "20211214" version

* Wed Dec 22 2021 Artem Polishchuk <ego.cordatus@gmail.com> - 0.0.20211214-1
- Update to 20211214

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.20201112-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.20201112-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Dec 15 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.0.20201112-1
- Update to 20201112

* Mon Dec 14 2020 Joe Walker <grumpey0@gmail.com> - 0.0.20200710-3
- Disable deduplication to fix problems with flatpak apps.

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.20200710-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jul 23 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.0.20200710-1
- Update to 20200710

* Mon May 25 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.0.20200511-1
- Update to 20200511

* Fri Mar 27 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.0.20200116-1
- Update to 20200116

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.20191223-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 03 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.0.20191223-1
- Update to 20191223

* Fri Sep 13 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0.0.20190908-3
- Update to 20190908
- Add recommended optional packages for complete theme

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.20190413-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Apr 21 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0.0.20190413-1
- Initial package
