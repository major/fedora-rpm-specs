Name: reversal-icon-theme
%global repo_name Reversal-icon-theme

Summary: Colorful icon theme inspired by Mac OS X aesthetic
License: GPL-3.0-only

%global git_date    20260317
%global git_commit  2c8122287e3bad5a6bf860ddd8c7e3b78cf4d451
%global git_commit_short  %(c="%{git_commit}"; echo ${c:0:7})

Version: 0^%{git_date}.git%{git_commit_short}
Release: 1%{?dist}

URL: https://github.com/yeyushengfan258/%{repo_name}
Source0: %{url}/archive/%{git_commit}/%{repo_name}-%{git_commit}.tar.gz

# Fix install script producing absolute symlinks
Patch0: 0000-install-fix.patch

BuildArch: noarch

Requires: hicolor-icon-theme


%description
Reversal is a colorful icon theme inspired by the aesthetic of Mac OS X.

Comes in a regular and dark variant.


%prep
%autosetup -n %{repo_name}-%{git_commit}

# Remove spurious executable bits found on some files
chmod 644 ./AUTHORS ./COPYING
find links/ src/ -executable -type f -exec chmod -v -- a-x '{}' '+'

# Do not call gtk-update-icon-cache during install
sed  \
	-e '/gtk-update-icon-cache/d'  \
	-i install.sh


%build
# Nothing to do here


%install
install -m 755 -d '%{buildroot}%{_datadir}/icons'
./install.sh --dest '%{buildroot}%{_datadir}/icons'

for VARIANT in '' '-dark'; do
	pushd "%{buildroot}%{_datadir}/icons/Reversal${VARIANT}"

	# Remove broken symlinks
	find ./ -follow -type l -printf 'deleted broken symlink "%p" -> "%l"\n' -delete

	# Create empty file for the cache
	touch icon-theme.cache

	# Remove these files (we will include them via %%doc/%%license macros)
	rm AUTHORS COPYING
	popd
done


%transfiletriggerin -- %{_datadir}/icons/Reversal
gtk-update-icon-cache --force %{_datadir}/icons/Reversal &>/dev/null || :

%transfiletriggerin -- %{_datadir}/icons/Reversal-dark
gtk-update-icon-cache --force %{_datadir}/icons/Reversal-dark &>/dev/null || :


%files
%doc AUTHORS
%license COPYING

# -- normal variant

%dir %{_datadir}/icons/Reversal
%ghost %{_datadir}/icons/Reversal/icon-theme.cache
%{_datadir}/icons/Reversal/index.theme

%{_datadir}/icons/Reversal/actions
%{_datadir}/icons/Reversal/actions@2x
%{_datadir}/icons/Reversal/animations
%{_datadir}/icons/Reversal/animations@2x
%{_datadir}/icons/Reversal/apps
%{_datadir}/icons/Reversal/apps@2x
%{_datadir}/icons/Reversal/categories
%{_datadir}/icons/Reversal/categories@2x
%{_datadir}/icons/Reversal/devices
%{_datadir}/icons/Reversal/devices@2x
%{_datadir}/icons/Reversal/emblems
%{_datadir}/icons/Reversal/emblems@2x
%{_datadir}/icons/Reversal/emotes
%{_datadir}/icons/Reversal/emotes@2x
%{_datadir}/icons/Reversal/mimes
%{_datadir}/icons/Reversal/mimes@2x
%{_datadir}/icons/Reversal/places
%{_datadir}/icons/Reversal/places@2x
%{_datadir}/icons/Reversal/preferences
%{_datadir}/icons/Reversal/preferences@2x
%{_datadir}/icons/Reversal/status
%{_datadir}/icons/Reversal/status@2x

# -- dark variant

%dir %{_datadir}/icons/Reversal-dark
%ghost %{_datadir}/icons/Reversal-dark/icon-theme.cache
%{_datadir}/icons/Reversal-dark/index.theme

%{_datadir}/icons/Reversal-dark/actions
%{_datadir}/icons/Reversal-dark/actions@2x
%{_datadir}/icons/Reversal-dark/animations
%{_datadir}/icons/Reversal-dark/animations@2x
%{_datadir}/icons/Reversal-dark/apps
%{_datadir}/icons/Reversal-dark/apps@2x
%{_datadir}/icons/Reversal-dark/categories
%{_datadir}/icons/Reversal-dark/categories@2x
%{_datadir}/icons/Reversal-dark/devices
%{_datadir}/icons/Reversal-dark/devices@2x
%{_datadir}/icons/Reversal-dark/emblems
%{_datadir}/icons/Reversal-dark/emblems@2x
%{_datadir}/icons/Reversal-dark/emotes
%{_datadir}/icons/Reversal-dark/emotes@2x
%{_datadir}/icons/Reversal-dark/mimes
%{_datadir}/icons/Reversal-dark/mimes@2x
%{_datadir}/icons/Reversal-dark/places
%{_datadir}/icons/Reversal-dark/places@2x
%{_datadir}/icons/Reversal-dark/preferences
%{_datadir}/icons/Reversal-dark/preferences@2x
%{_datadir}/icons/Reversal-dark/status
%{_datadir}/icons/Reversal-dark/status@2x


%changelog
* Tue Aug 18 2026 Artur Frenszek-Iwicki <fedora@svgames.pl> - 0^20260317.git2c81222-1
- Update to latest git snapshot

* Sun Aug 31 2025 Artur Frenszek-Iwicki <fedora@svgames.pl> - 0^20250826.1bdf4c6-1
- Update to latest git snapshot

* Sat Sep 16 2023 Artur Frenszek-Iwicki <fedora@svgames.pl> - 0^20230513.bdae2ea-1
- Initial packaging
