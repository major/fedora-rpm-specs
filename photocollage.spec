Summary:        Graphical tool to make photo collage posters
Name:           photocollage
Version:        1.4.5
Release:        %autorelease
Url:            https://github.com/adrienverge/PhotoCollage
License:        GPLv2+

Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  python3-devel >= 3.5
BuildRequires:  python3-setuptools
BuildRequires:  gettext
BuildRequires:  desktop-file-utils

Requires:       python3-pillow >= 2.0
Requires:       python3-cairo >= 1.10
Requires:       python3-gobject >= 3.0
Requires:       python3-six
Requires:       gettext-runtime >= 0.18

%description
PhotoCollage allows you to create photo collage posters. It assembles
the input photographs it is given to generate a big poster. Photos are
automatically arranged to fill the whole poster, then you can change the
final layout, dimensions, border or swap photos in the generated grid.
Eventually the final poster image can be saved in any size.

%prep
%autosetup -n PhotoCollage-%{version}

%build
%{__python3} setup.py build

%install
%{__python3} setup.py install -O1 --root %{buildroot}
%find_lang %{name}
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%files -f %{name}.lang
%doc README.rst
%license LICENSE
%{python3_sitelib}/*
%{_bindir}/photocollage
%{_datadir}/applications/%{name}.desktop
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/icons/hicolor/*/apps/%{name}.png

%changelog
%autochangelog
