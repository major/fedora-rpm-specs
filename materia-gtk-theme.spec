# WIP: split into sub packages

%global vergit 20210322

Name:           materia-gtk-theme
Version:        0.0.%{vergit}
Release:        5%{?dist}
Summary:        Material Design theme for GNOME/GTK based desktop environments
BuildArch:      noarch

License:        GPLv2
URL:            https://github.com/nana-4/materia-theme
Source0:        %{url}/archive/v%{vergit}/%{name}-%{version}.tar.gz

BuildRequires:  gnome-shell
BuildRequires:  meson
BuildRequires:  sassc

Requires:       filesystem

Suggests:       flat-remix-icon-theme
Suggests:       papirus-icon-theme

%description
Materia is a Material Design theme for GNOME/GTK based desktop environments.

It supports GTK 2, GTK 3, GNOME Shell, Budgie, Cinnamon, MATE, Unity, Xfce,
LightDM, GDM, Chrome theme, etc.


%prep
%autosetup -n materia-theme-%{vergit} -p1


%build
%meson
%meson_build


%install
%meson_install
find %{buildroot}%{_datadir}/themes -name "COPYING" -exec rm -rf {} \;
find %{buildroot}%{_datadir}/themes -name "index.theme" -exec chmod -x {} \;


# Workaround for RH#1944886
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Directory_Replacement/#_scriptlet_to_replace_a_directory
%pretrans -p <lua>
path = "%{_datadir}/themes/Materia/gtk-3.0"
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

path = "%{_datadir}/themes/Materia-compact/gtk-3.0"
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

path = "%{_datadir}/themes/Materia-dark-compact/gtk-3.0"
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

path = "%{_datadir}/themes/Materia-dark/gtk-3.0"
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

path = "%{_datadir}/themes/Materia-light-compact/gtk-3.0"
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

path = "%{_datadir}/themes/Materia-light/gtk-3.0"
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


%files
%license COPYING
%doc README.md HACKING.md TODO.md
%{_datadir}/themes/Materia*/


%changelog
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.20210322-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.20210322-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.20210322-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Mar 31 2021 Artem Polishchuk <ego.cordatus@gmail.com> - 0.0.20210322-2
- build: Workaround for RH#1944886

* Mon Mar 22 2021 Artem Polishchuk <ego.cordatus@gmail.com> - 0.0.20210322-1
- build(update): 20210322

* Sun Mar 07 2021 Artem Polishchuk <ego.cordatus@gmail.com> - 0.0.20200916-3
- Fix FTBFS 34

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.20200916-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Sep 16 21:53:06 EEST 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.0.20200916-1
- Update to 20200916

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.20200320-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Mar 27 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.0.20200320-1
- Update to 20200320

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.20191017-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Jan 05 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.0.20191017-1
- Update to 20191017

* Tue Sep 24 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0.0.20190912-1
- Initial package
