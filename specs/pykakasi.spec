%global __python /usr/bin/python3
Name:           pykakasi
Version:        2.3.0
Release:        3%{?dist}
Summary:        Lightweight converter from Japanese Kana-kanji sentences into Kana-Roman

License:        GPL-3.0-or-later AND BSD-3-Clause
URL:            https://codeberg.org/miurahr/pykakasi
Source:         https://codeberg.org/miurahr/pykakasi/archive/v%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-sphinx make

%global _description %{expand:
a Python Natural Language Processing (NLP) library to transliterate hiragana,
katakana and kanji (Japanese text) into rōmaji (Latin/Roman alphabet).
It can handle characters in NFC form.}

%description %_description

%prep
%autosetup -p1 -n %{name}
%py3_shebang_fix src/pykakasi/cli.py

%generate_buildrequires
%pyproject_buildrequires -t

%build
%pyproject_wheel
sphinx-build docs build/docs -b man -d man
ls -lR build/docs/

%install
%pyproject_install
%pyproject_save_files -l pykakasi
chmod 0755 %{buildroot}/%{python_sitelib}/pykakasi/cli.py
mkdir -p %{buildroot}/%{_mandir}/man1
cp -a build/docs/pykakasi.1 %{buildroot}/%{_mandir}/man1/

%check
%pytest -k 'not test_aozora'

%files -n pykakasi -f %{pyproject_files}
%{_bindir}/kakasi
%{_mandir}/man1/pykakasi.1.gz
%doc docs/*rst
%doc docs/*rst.inc

%changelog
* Sat Jan 18 2025 Kevin Fenzi <kevin@scrye.com> - 2.3.0-3
- Build/ship man page version of docs
- Fix permissions on cli.py

* Wed Jan 01 2025 Kevin Fenzi <kevin@scrye.com> - 2.3.0-2
- Various fixes and updates from review

* Sat Nov 30 2024 Kevin Fenzi <kevin@scrye.com> - 2.3.0-1
- Initial version
