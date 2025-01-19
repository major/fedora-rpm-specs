Name:		numix-gtk-theme
Version:	2.6.7
Release:	16%{?dist}
Summary:	Numix Gtk Theme

Source:		https://github.com/numixproject/numix-gtk-theme/archive/%{version}.tar.gz#/numix-gtk-theme-%{version}.tar.gz

# Automatically converted from old format: GPLv3 - review is highly recommended.
License:	GPL-3.0-only
URL:		https://github.com/numixproject/numix-gtk-theme

BuildArch:	noarch

BuildRequires: make
BuildRequires:	rubygem-sass
BuildRequires:	gdk-pixbuf2-devel
Requires:	filesystem
Requires:	gtk-murrine-engine

%description
Numix is a modern flat theme with a combination of light and dark elements.
It supports Gnome, Unity, XFCE and Openbox.

%prep
%autosetup -n %{name}-%{version}

%build
find -type f -executable -exec chmod -x {} \;

%install
chmod +x scripts/utils.sh
%make_install

%files
%license LICENSE
%doc README.md
%doc CREDITS
%{_datadir}/themes/Numix

# This is to clean up directories before links created
# See https://bugzilla.redhat.com/show_bug.cgi?id=1379883
# See https://fedoraproject.org/wiki/Packaging:Directory_Replacement
%pretrans -p <lua>
directories = {
  "/usr/share/themes/Numix/gtk-3.0/assets",
  "/usr/share/themes/Numix/gtk-3.2/assets"
}
for i,path in ipairs(directories) do
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
end


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.7-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Jul 29 2024 Miroslav Suchý <msuchy@redhat.com> - 2.6.7-15
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.7-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.7-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.7-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.7-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.7-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.7-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.7-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Oct 09 2018 Brendan Early <mymindstorm1@gmail.com> - 2.6.7-1
- Update to release 2.6.7
- Bring more in line with packaging guidelines

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Apr 18 2017 Fedora <sspreitz@redhat.com> - 2.6.6-2
- move directories prior to symlink creation
- See https://bugzilla.redhat.com/show_bug.cgi?id=1379883
- See https://fedoraproject.org/wiki/Packaging:Directory_Replacement

* Tue Apr 18 2017 Fedora <sspreitz@redhat.com> - 2.6.6-1
- new version

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Sep 24 2016 Sascha Spreitzer <sspreitz@redhat.com> - 2.6.4-1
- new version

* Tue Jun 14 2016 Sascha Spreitzer <sspreitz@redhat.com> - 2.6.0-1
- Bump version

* Tue Jun 14 2016 Sascha Spreitzer <sspreitz@redhat.com> - 2.5.1-5.gitbde0a73
- rebuilt

* Mon Jun 13 2016 Sascha Spreitzer <sspreitz@redhat.com> - 2.5.1-4.gitbde0a73
- Fix file permissions

* Tue May 31 2016 Sascha Spreitzer <sspreitz@redhat.com> - 2.5.1-3.gitbde0a73
- spec file fixes

* Wed Apr 20 2016 Sascha Spreitzer <sspreitz@redhat.com> - 2.5.1-2.gitbde0a73
- license tag for license file, diffable lines

* Tue Apr 19 2016 Sascha Spreitzer <sspreitz@redhat.com> - 2.5.1-1.gitbde0a73
- split spec file

* Sat Apr 16 2016 Sascha Spreitzer <sspreitz@redhat.com> - 0.1.0-6.gitbde0a73
- adjust groups and tabstops

* Sat Apr 16 2016 Sascha Spreitzer <sspreitz@redhat.com> - 0.1.0-5.gitbde0a73
- fix sources setup and relative dirs

* Sat Apr 16 2016 Sascha Spreitzer <sspreitz@redhat.com> - 0.1.0-4.gitbde0a73
- add license and readme files

* Sat Apr 16 2016 Sascha Spreitzer <sspreitz@redhat.com> - 0.1.0-3.gitbde0a73
- require gdk-pixbuf2

* Sat Apr 16 2016 Sascha Spreitzer <sspreitz@redhat.com> - 0.1.0-2.gitbde0a73
- refactor for git use

* Sun Jan 24 2016 Sascha Spreitzer <sspreitz@redhat.com> - 0.1.0-1.gitbde0a73
- Refactor to build real srpms
- Repackaging
- Adding Shine and uTouch

