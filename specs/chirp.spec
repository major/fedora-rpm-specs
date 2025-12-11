%global ver 0.4.0
%global version_strip_caret %(VER='%{version}'; echo "${VER/^*/}")
%global version_snap %(VER='%{version}'; echo "${VER/*^/}")

Name:		chirp
Version:	%{ver}^20251205
Release:	%autorelease
Summary:	A tool for programming two-way radio equipment

License:	GPL-3.0-or-later
URL:		http://chirp.danplanet.com/
Source0:	https://archive.chirpmyradio.com/chirp_next/next-%{version_snap}/%{name}-%{version_snap}.tar.gz
Source1:	com.danplanet.CHIRP.metainfo.xml

BuildArch:	noarch

BuildRequires:	coreutils
BuildRequires:	sed
BuildRequires:	gettext
BuildRequires:	make
BuildRequires:	python3-devel

# for tests
BuildRequires:	python3dist(pytest)
BuildRequires:	python3-pyyaml
BuildRequires:	python3-ddt

BuildRequires:	desktop-file-utils
BuildRequires:	hicolor-icon-theme
Requires:	hicolor-icon-theme


%description
Chirp is a tool for programming two-way radio equipment It provides a generic
user interface to the programming data and process that can drive many radio
models under the hood.


%prep
%autosetup -p1 -n %{name}-%{version_snap}

# Fix version
sed -i 's/\(\bversion\s*=\s*\)0\b/\1"%{version_strip_caret}"/' setup.py

# Rename package to avoid pypi conflict
sed -i 's/\(\bname\s*=\s*'"'"'\)chirp'"'"'/\1chirp-project'"'"'/' setup.py
mv chirp.egg-info chirp_project.egg-info

%generate_buildrequires
%pyproject_buildrequires -x wx


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files chirp

# Locale
mkdir -p %{buildroot}%{_datadir}/locale
ln -frs %{buildroot}%{_datadir}/locale \
  %{buildroot}%{python3_sitelib}/chirp/locale
%find_lang CHIRP

# Install files to correct location
desktop-file-install \
  --dir=%{buildroot}%{_datadir}/applications \
  %{buildroot}%{python3_sitelib}/chirp/share/chirp.desktop
install -Dpm 0644 %{buildroot}%{python3_sitelib}/chirp/share/chirp.svg \
  %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/chirp.svg
install -Dpm 0644 %{SOURCE1} \
  %{buildroot}%{_metainfodir}/com.danplanet.CHIRP.metainfo.xml
install -Dpm 0644 %{buildroot}%{python3_sitelib}/chirp/share/chirpw.1 \
  %{buildroot}%{_mandir}/man1/chirp.1
# Symlink to resources
ln -frs %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/chirp.svg \
  %{buildroot}%{python3_sitelib}/chirp/share/chirp.svg
ln -frs %{buildroot}%{_datadir}/applications/chirp.desktop \
  %{buildroot}%{python3_sitelib}/chirp/share/chirp.desktop
ln -frs %{buildroot}%{_mandir}/man1/chirp.1.gz \
  %{buildroot}%{python3_sitelib}/chirp/share/chirpw.1


%check
# Disabled, too time and memory expensive
#%%pytest


%files -f %{pyproject_files} -f CHIRP.lang
%license COPYING
%doc README.md
%{_bindir}/chirpc
%{_bindir}/experttune
%{python3_sitelib}/chirp/locale

%pyproject_extras_subpkg -n chirp wx
%{_bindir}/chirp
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/scalable/apps/chirp.svg
%{_metainfodir}/com.danplanet.CHIRP.metainfo.xml
%{_mandir}/man1/chirp.1.gz


%changelog
%autochangelog
