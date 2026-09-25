%bcond_without  nm_icons


Name:           mint-x-icons
Version:        1.7.7
Release:        %autorelease
Summary:        Icon theme for Linux Mint

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            http://linuxmint.com
Source0:        http://packages.linuxmint.com/pool/main/m/%{name}/%{name}_%{version}.tar.xz

BuildArch:      noarch

BuildRequires:  fdupes

Requires:       filesystem
Requires:       gnome-icon-theme
Requires:       hicolor-icon-theme

%description
%{summary}.


%prep
%autosetup -c


%build
%if %{with nm_icons}
# Remove icons for nm-applet, because they are ugly.
%{_bindir}/find %{name}%{_prefix} -name "nm-*" -type f -delete
%{_bindir}/find %{name}%{_prefix} -name "nm-*" -xtype l			\
  -exec %{_bindir}/unlink {} \;
%{_bindir}/find %{name}%{_prefix} -name 'gnome-netstatus*' -xtype l	\
  -exec %{__file} {} \; | %{__grep} 'broken' |			\
  %{__sed} -e 's!:[ \t]\+.*$!!g' |				\
  %{_bindir}/xargs --max-args=1 %{_bindir}/unlink
%endif


%install
%{__cp} -pr %{name}%{_prefix} %{buildroot}
%fdupes -s %{buildroot}


%transfiletriggerin -- %{_datadir}/icons/Mint-X
for _dir in %{_datadir}/icons/Mint-X*/ ; do
  %{_bindir}/gtk-update-icon-cache --force ${_dir} &>/dev/null || :
done


%transfiletriggerpostun -- %{_datadir}/icons/Mint-X
for _dir in %{_datadir}/icons/Mint-X*/ ; do
  %{_bindir}/gtk-update-icon-cache --force ${_dir} &>/dev/null || :
done


%files
%license %{name}/debian/copyright
%doc %{name}/debian/changelog
%{_datadir}/icons/Mint-X*
%{_datadir}/folder-color-switcher/


%changelog
%autochangelog