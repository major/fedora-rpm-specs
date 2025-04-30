%global forgeurl https://github.com/UshakovVasilii/gnome-shell-extension-freon

Name:           gnome-shell-extension-freon
Epoch:          2
Version:        58
%global srcversion EGO-%{version}
Release:        %autorelease
Summary:        GNOME Shell extension to display system temperature, voltage, and fan speed

License:        GPL-2.0-only
URL:            %{forgeurl}/wiki
Source:         %{forgeurl}/archive/%{srcversion}/%{name}-%{srcversion}.tar.gz

BuildRequires:  glib2

# Dependencies described here:
# https://github.com/UshakovVasilii/gnome-shell-extension-freon/wiki/Dependency
%if 0%{?fedora} >= 42
BuildRequires:  gnome-shell-rpm-generators
%else
Requires:       gnome-shell >= 45
%endif

Requires:       gnome-shell-extension-common
Requires:       lm_sensors
Recommends:     nvme-cli

BuildArch:      noarch

%description
Freon is a GNOME Shell extension for displaying the temperature of your
CPU, hard disk, solid state, and video card (NVIDIA, Catalyst, and
Bumblebee supported), as well as power supply voltage, and fan
speed. You can choose which HDD/SSD or other devices to include, what
temperature units to use, and how often to refresh the sensors readout,
and they will appear in the GNOME Shell top bar.

# UUID is defined in extension's metadata.json and used as directory name.
%global  UUID                  freon@UshakovVasilii_Github.yahoo.com
%global  gnome_extensions_dir  %{_datadir}/gnome-shell/extensions/
%global  final_install_dir     %{buildroot}/%{gnome_extensions_dir}/%{UUID}

%prep
%autosetup -n %{name}-%{srcversion}

cat > ./README-fedora.md << EOF
**NOTE** that if you want to see GPU temperature, you will need to
install the vendor's official driver and any related packages. (Nouveau
unfortunately won't work for Nvidia cards.)

- hard drive temperatures requires that you probe the `drivetemp.ko`
  kernel module. One way is to add the file
  /etc/modules-load.d/drivetemp.conf with a single line saying
  drivetemp
- Nvidia GPU temperatures require the `nvidia-settings` application,
  typically installed with the proprietary Nvidia drivers
- AMD GPU temperatures requires `aticonfig`, part of AMD Radeon Software
  (formerly known as AMD Catalyst)
- Bumblebee + Nvidia requires `optirun`

You can read more about this and other tips
**on the Freon [wiki](https://github.com/UshakovVasilii/gnome-shell-extension-freon/wiki)**.

Also, after installing this GNOME Shell extension, each user that wants
it must still manually enable Freon before it will take effect. You can
do so a few different ways.

First, restart GNOME Shell (Open the command dialog with Alt-F2, type
\`r\`, and hit enter), or log out and log back in. Then:

- If you've already set up the GNOME Shell web browser plugin, go to
  <https://extensions.gnome.org/local/>, find the extension, and click
  the switch to "ON."
- Open GNOME Tweaks, go to the Extensions tab, find the extension,
  and click the switch to "ON."
- Open a terminal or the desktop's command dialog, and (as your normal
  user account) run:
  \`gnome-extensions enable %{UUID}\`
EOF



%build
# No compilation necessary.



%install
mkdir -p %{final_install_dir}
cp --recursive --preserve=mode,timestamps  %{UUID}/*  %{final_install_dir}

# RPM will take care of gschemas, but they should be installed to system-wide directory.
mkdir -p %{buildroot}/%{_datadir}/glib-2.0/schemas/
mv  %{final_install_dir}/schemas/org.gnome.shell.extensions.sensors.gschema.xml  \
    %{buildroot}/%{_datadir}/glib-2.0/schemas/
rmdir %{final_install_dir}/schemas/

# Remove source .po localization files, move binary .mo to system directory.
mv  %{final_install_dir}/locale  %{buildroot}/%{_datadir}/

%find_lang freon



%files -f freon.lang
%doc README.md  README-fedora.md
%license LICENSE
%{gnome_extensions_dir}/%{UUID}/
%{_datadir}/glib-2.0/schemas/org.gnome.shell.extensions.sensors.gschema.xml



%changelog
%autochangelog
