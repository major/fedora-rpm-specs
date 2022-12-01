%global upstream_name manpages-l10n

%global distribution fedora-rawhide

%global translations \
    cs:    "Czech" \
    da:    "Danish" \
    de:    "German" \
    el:    "Greek" \
    es:    "Spanish" \
    fi:    "Finnish" \
    fr:    "French" \
    hu:    "Hungarian" \
    id:    "Indonesian" \
    it:    "Italian" \
    mk:    "Macedonian" \
    nl:    "Dutch" \
    nb:    "Norwegian Bokmål" \
    pl:    "Polish" \
    pt_BR: "Portuguese (Brazil)" \
    ro:    "Romanian" \
    sr:    "Serbian" \
    sv:    "Swedish" \
    uk:    "Ukrainian" \
    vi:    "Vietnamese"

Name:           man-pages-l10n
Version:        4.16.0
Release:        1%{?dist}
Summary:        Translated man pages from the Linux Documentation Project and other software projects

# original man pages are under various licenses, translations are GPLv3+
# generated from upstream/fedora-rawhide/packages.txt with:
#   dnf --disablerepo=* --enablerepo=rawhide repoquery --queryformat "%%{license}" $(<upstream/fedora-rawhide/packages.txt) |\
#   sed 's/) and (/)\n(/g;s/) and /)\n/g;s/ and (/\n(/g' |\
#   sed '/^(/!s/\(.* or .*\)/(\1)/' |\
#   sed '/^(/!s/ and /\n/g' |\
#   (echo GPLv3+ && cat) |\
#   sort -u
License:        Artistic Licence 2.0 and BSD and BSD with advertising and Copyright only and GFDL and GPL+ and GPLv2 and GPLv2+ and (GPLv2+ or Artistic) and GPLv2 with exceptions and GPLv2+ with exceptions and GPLv3+ and (GPLv3+ and BSD) and (GPLv3+ or BSD) and IJG and ISC and LGPLv2+ and LGPLv3+ and (LGPLv3+ or BSD) and MIT and psutils and Public Domain and Sendmail and Verbatim

URL:            https://manpages-l10n-team.pages.debian.net/manpages-l10n/
Source0:        https://salsa.debian.org/manpages-l10n-team/%{upstream_name}/-/archive/%{version}/%{upstream_name}-v%{version}.tar.bz2

BuildArch:      noarch

BuildRequires:  make
BuildRequires:  po4a


%description
Translated man pages from the Linux Documentation Project
and other software projects.


# generate subpackages
%{lua: for code, name in rpm.expand('%{translations}'):gmatch('(%S+):%s+(%b"")') do
    name = name:gsub('"', '')

    print('%package -n man-pages-' .. code .. '\n')
    print('Summary: ' .. name .. ' man pages from the Linux Documentation Project\n')
    print('Requires: man-pages-reader\n')
    print('Supplements: (man-pages and langpacks-' .. code .. ')\n')

    -- obsolete man-pages-es-extra
    if code == 'es' then
        print('Obsoletes: man-pages-es-extra < 1.55-36\n')
    end

    print('%description -n man-pages-' .. code .. '\n')
    print('Manual pages from the Linux Documentation Project, translated into ' .. name .. '.\n')
end}


%prep
%autosetup -p1 -n %{upstream_name}-v%{version}


%build
%configure --enable-distribution=%{distribution}
%make_build


%install
%make_install
# prevent conflict with net-tools
rm %{buildroot}%{_mandir}/de/man5/ethers.5*


# generate %files sections
%{lua: for code in rpm.expand('%{translations}'):gmatch('(%S+):%s+%b""') do
    print('%files -n man-pages-' .. code .. '\n')
    print('%license LICENSE COPYRIGHT.md\n')
    print('%doc AUTHORS.md CHANGES.md README.md\n')
    print(rpm.expand('%{_mandir}') .. '/' .. code .. '/man*/*\n')
end}


%changelog
* Fri Nov 25 2022 Lukas Javorsky <ljavorsk@redhat.com> - 4.16.0-1
- Rebase to version 4.16.0

* Sat Aug 13 2022 Nikola Forró <nforro@redhat.com> - 4.15.0-2
- Prevent conflict with net-tools

* Thu Aug 11 2022 Nikola Forró <nforro@redhat.com> - 4.15.0-1
- Update to version 4.15.0
  resolves: #2117044

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.14.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri May 06 2022 Nikola Forró <nforro@redhat.com> - 4.14.0-1
- Update to version 4.14.0
  resolves: #2081822

* Fri Feb 25 2022 Nikola Forró <nforro@redhat.com> - 4.13-1
- Update to version 4.13
  resolves: #2057369

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.12.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Dec 21 2021 Nikola Forró <nforro@redhat.com> - 4.12.1-1
- Update to version 4.12.1
  resolves: #2033989

* Mon Oct 11 2021 Nikola Forró <nforro@redhat.com> - 4.11.0-2
- Reenable Spanish translation

* Wed Sep 15 2021 Nikola Forró <nforro@redhat.com> - 4.11.0-1
- Update to version 4.11.0
  resolves: #2004244

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jun 16 2021 Nikola Forró <nforro@redhat.com> - 4.10.0-1
- Update to version 4.10.0
  resolves: #1971334

* Thu Mar 11 2021 Nikola Forró <nforro@redhat.com> - 4.9.3-1
- Update to version 4.9.3
  resolves: #1937093

* Thu Feb 18 2021 Nikola Forró <nforro@redhat.com> - 4.9.2-3
- Temporarily disable Spanish translation
  resolves: #1929938

* Thu Feb 11 2021 Nikola Forró <nforro@redhat.com> - 4.9.2-2
- Obsolete man-pages-es-extra

* Thu Feb 11 2021 Nikola Forró <nforro@redhat.com> - 4.9.2-1
- Update to version 4.9.2
  resolves: #1925829

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Oct 15 2020 Rafael Fontenelle <rafaelff@gnome.org> - 4.2.0-1
- Update to version 4.2.0

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 03 2020 Nikola Forró <nforro@redhat.com> - 4.1.0-1
- Update to version 4.1.0
  resolves: #1852799

* Sun Mar 22 2020 Nikola Forró <nforro@redhat.com> - 4.0.0-1.20200322gitbff338d
- Remove man pages provided by xz-5.2.5
- Update to the latest commit

* Wed Mar 18 2020 Nikola Forró <nforro@redhat.com> - 4.0.0-1.20200318gite5c0d56
- Fix summary and description
- Update to the latest commit

* Tue Mar 17 2020 Nikola Forró <nforro@redhat.com> - 4.0.0-1.20200317gitb4ac9e9
- Initial package
