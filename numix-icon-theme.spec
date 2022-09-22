%global forgeurl    https://github.com/numixproject/numix-icon-theme
%global tag         %{version}

%forgemeta

Name:		numix-icon-theme
Summary:	Numix Project icon theme
Version:	21.10.31
Release:	%autorelease
License:	GPLv3

URL:		%{forgeurl}
Source:     %{forgesource}

BuildArch:	noarch
Requires:	filesystem
Requires:	gnome-icon-theme
Requires:	hicolor-icon-theme

%description
Numix is the official icon theme from the Numix project.
It is heavily inspired by, and based upon parts of the Elementary,
Humanity and Gnome icon themes.

%prep
%forgesetup

%build
find -type f -executable -exec chmod -x {} \;

%install
install -d %{buildroot}%{_datadir}/icons

mkdir -p %{buildroot}%{_datadir}/doc/%{name}
cp -pr Numix %{buildroot}%{_datadir}/icons/Numix
cp -pr Numix-Light %{buildroot}%{_datadir}/icons/Numix-Light

%post
/bin/touch --no-create %{_datadir}/icons/Numix &>/dev/null || :
/bin/touch --no-create %{_datadir}/icons/Numix-Light &>/dev/null || :

%postun
if [ $1 -eq 0 ] ; then
    /bin/touch --no-create %{_datadir}/icons/Numix &>/dev/null
    /bin/touch --no-create %{_datadir}/icons/Numix-Light &>/dev/null
    /usr/bin/gtk-update-icon-cache %{_datadir}/icons/Numix &>/dev/null || :
    /usr/bin/gtk-update-icon-cache %{_datadir}/icons/Numix-Light &>/dev/null || :
fi

%posttrans
/usr/bin/gtk-update-icon-cache %{_datadir}/icons/Numix &>/dev/null || :
/usr/bin/gtk-update-icon-cache %{_datadir}/icons/Numix-Light &>/dev/null || :

%files
%license license
%doc readme.md
%{_datadir}/icons/Numix
%{_datadir}/icons/Numix-Light

%changelog
%autochangelog
