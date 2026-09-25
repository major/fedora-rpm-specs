Name:           mint-y-icons
Version:        1.9.4
Release:        %autorelease
Summary:        The Mint-Y icon theme

License:        CC-BY-SA-4.0 AND GPL-3.0-or-later
URL:            https://github.com/linuxmint/%{name}
Source0:        %url/archive/%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  fdupes

Requires:       adwaita-icon-theme
Requires:       hicolor-icon-theme

%description
%{summary}.

%prep
%autosetup

%build

%install
cp -pr ${PWD}%{_prefix} %{buildroot}
%fdupes -s %{buildroot}

%transfiletriggerin -- %{_datadir}/icons/Mint-Y
for _dir in %{_datadir}/icons/Mint-Y*/ ; do
  %{_bindir}/gtk-update-icon-cache --force ${_dir} &>/dev/null || :
done

%transfiletriggerpostun -- %{_datadir}/icons/Mint-Y
for _dir in %{_datadir}/icons/Mint-Y*/ ; do
  %{_bindir}/gtk-update-icon-cache --force ${_dir} &>/dev/null || :
done

%files
%license debian/copyright
%doc debian/changelog
%doc README.md
%{_datadir}/icons/Mint-*/
%{_datadir}/folder-color-switcher/

%changelog
%autochangelog