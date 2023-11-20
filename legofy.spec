# Pull from GitHub, since it has fixes not released on PyPI and contains
# the LICENSE file as well as an additional doc.
%global forgeurl https://github.com/JuanPotato/Legofy
%global commit 0cadceb9f412636c11eb62370682a43ae329e4cb

Name:           legofy
Version:        1.0.0
Release:        %autorelease
Summary:        Make images look as if they are made out of 1x1 LEGO blocks
%forgemeta
# SPDX identifier
License:        MIT
URL:            %forgeurl
Source0:        %forgesource
Source1:        %{name}.1

BuildArch:      noarch
BuildRequires:  python3-devel

%description
Legofy is a python program that takes a static image or gif and makes
it so that it looks as if it was built out of LEGO.


%prep
%forgeautosetup -p1


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files %{name}
install -pDm644 %{SOURCE1} %{buildroot}%{_mandir}/man1/legofy.1


%files -f %{pyproject_files}
%{_bindir}/%{name}
%{_mandir}/man1/%{name}*
%doc README.md 2010-LEGO-color-palette.pdf


%changelog
%autochangelog
