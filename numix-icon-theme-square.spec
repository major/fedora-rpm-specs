%global forgeurl    https://github.com/numixproject/numix-icon-theme-square
%global tag         %{version}

%forgemeta

Name:           numix-icon-theme-square
Summary:        Numix Project square icon theme
Version:        21.12.05
Release:        %autorelease
License:        GPLv3

URL:            %{forgeurl}
Source:         %{forgesource}

BuildArch:      noarch
Requires:       numix-icon-theme

%description
Numix Square is a modern icon theme for Linux from the Numix project.

%prep
%forgesetup

%install
mkdir -p %{buildroot}%{_datadir}/icons
cp -pr Numix-Square %{buildroot}%{_datadir}/icons/Numix-Square
cp -pr Numix-Square-Light %{buildroot}%{_datadir}/icons/Numix-Square-Light

%post
touch -c %{_datadir}/icons/Numix-Square &>/dev/null || :
touch -c %{_datadir}/icons/Numix-Square-Light &>/dev/null || :

%postun
if [ $1 -eq 0 ] ; then
    touch -c %{_datadir}/icons/Numix-Square &>/dev/null
    touch -c %{_datadir}/icons/Numix-Square-Light &>/dev/null
    gtk-update-icon-cache %{_datadir}/icons/Numix-Square &>/dev/null || :
    gtk-update-icon-cache %{_datadir}/icons/Numix-Square-Light &>/dev/null || :
fi

%posttrans
gtk-update-icon-cache %{_datadir}/icons/Numix-Square &>/dev/null || :
gtk-update-icon-cache %{_datadir}/icons/Numix-Square-Light &>/dev/null || :

%files
%license LICENSE
%doc README.md
%{_datadir}/icons/Numix-Square
%{_datadir}/icons/Numix-Square-Light

%changelog
%autochangelog
