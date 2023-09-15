# WIP: split into sub packages

%global vergit 20210322

Name:           materia-gtk-theme
Version:        0.0.%{vergit}
Release:        %autorelease
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
%autochangelog
