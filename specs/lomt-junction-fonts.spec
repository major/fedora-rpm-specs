%global commit fb73260e86dd301b383cf6cc9ca8e726ef806535
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global ghowner theleagueof
%global ghproject junction

Version: 0^20140329gitfb73260
Release: 6%{?dist}

URL: https://www.theleagueofmoveabletype.com/junction

%global foundry  LOMT
%global fontlicense  OFL-1.1
%global fontlicenses  OpenFontLicense.markdown

%global fontfamily  Junction
%global fontsummary A humanist sans-serif typeface
%global fontdescription  %{expand:Junction is a a humanist sans-serif,
and the first open-source type project started by The League of Moveable
Type. It has been updated (2014) to include additional weights (light/bold)
and expanded international support.}

%global fonts  *.otf
%global fontconfs  %{SOURCE10}

Source0: https://github.com/%{ghowner}/%{ghproject}/archive/%{commit}/%{ghproject}-%{shortcommit}.tar.gz
Source10: 60-%{fontpkgname}.xml
# https://github.com/theleagueof/junction/issues/16
Source11: update-names.pe
Source12: update-foundry.pe 

BuildRequires: fontforge

%fontpkg

%prep
%setup -q -n %{ghproject}-%{commit}
mv 'Open Font License.markdown' OpenFontLicense.markdown
mv 'Open Font License FAQ.markdown' OpenFontLicenseFAQ.markdown

%build
cp %{SOURCE11} .
cp %{SOURCE12} .
fontforge -script update-names.pe Junction-bold.otf Junction "Junction Bold" Bold temp.sfd
fontforge -script update-foundry.pe temp.sfd lomt Junction-bold.otf
fontforge -script update-names.pe Junction-regular.otf Junction "Junction" Regular temp.sfd
fontforge -script update-foundry.pe temp.sfd lomt Junction-regular.otf
fontforge -script update-names.pe Junction-light.otf Junction "Junction Light" Light temp.sfd
fontforge -script update-foundry.pe temp.sfd lomt Junction-light.otf

rm temp.sfd
rm update-names.pe
rm update-foundry.pe

%fontbuild


%install
%fontinstall


%check
%fontcheck


%fontfiles
%doc readme.markdown
%doc OpenFontLicenseFAQ.markdown

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0^20140329gitfb73260-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0^20140329gitfb73260-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0^20140329gitfb73260-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0^20140329gitfb73260-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0^20140329gitfb73260-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sun Jul 09 2023 Benson Muite <benson_muite@emailplus.org> - 0^20140329gitfb73260-1
- Add documentation files
- Rewrite the full name to match format guidelines of <family> <style>

* Thu Jun 29 2023 Benson Muite <benson_muite@emailplus.org> - 0^20140329gitfb73260-1
- Initial packaging
