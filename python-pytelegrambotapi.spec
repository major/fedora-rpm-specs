%global appname pytelegrambotapi
%global richname pyTelegramBotAPI

%global _description %{expand:
A simple, but extensible Python implementation for the Telegram
Bot API.

It can be used to create powerful bots for the Telegram messenger.}

Name: python-%{appname}
Version: 4.8.0
Release: 1%{?dist}

License: GPL-2.0-or-later
Summary: Python Telegram Bot API implementation
URL: https://github.com/eternnoir/%{richname}
Source0: %{url}/archive/%{version}/%{appname}-%{version}.tar.gz
BuildArch: noarch

BuildRequires: python3-devel
BuildRequires: python3-pytest

%description %_description

%package -n python3-%{appname}
Summary: %{summary}

%description -n python3-%{appname} %_description

%prep
%autosetup -n %{richname}-%{version} -p1

%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files telebot

%check
%pytest

%files -n python3-%{appname} -f %{pyproject_files}
%license LICENSE
%doc README.md

%changelog
* Wed Nov 30 2022 Vitaly Zaitsev <vitaly@easycoding.org> - 4.8.0-1
- Updated to version 4.8.0.

* Sat Oct 22 2022 Vitaly Zaitsev <vitaly@easycoding.org> - 4.7.1-1
- Updated to version 4.7.1.

* Tue Aug 16 2022 Vitaly Zaitsev <vitaly@easycoding.org> - 4.7.0-1
- Updated to version 4.7.0.

* Fri Jul 29 2022 Vitaly Zaitsev <vitaly@easycoding.org> - 4.6.1-1
- Updated to version 4.6.1.

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jun 23 2022 Vitaly Zaitsev <vitaly@easycoding.org> - 4.6.0-1
- Updated to version 4.6.0.

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 4.5.1-2
- Rebuilt for Python 3.11

* Sun May 08 2022 Vitaly Zaitsev <vitaly@easycoding.org> - 4.5.1-1
- Updated to version 4.5.1.

* Mon Apr 18 2022 Vitaly Zaitsev <vitaly@easycoding.org> - 4.4.1-1
- Updated to version 4.4.1.

* Wed Feb 02 2022 Vitaly Zaitsev <vitaly@easycoding.org> - 4.4.0-1
- Updated to version 4.4.0.

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Jan 10 2022 Vitaly Zaitsev <vitaly@easycoding.org> - 4.3.1-1
- Updated to version 4.3.1.

* Fri Dec 10 2021 Vitaly Zaitsev <vitaly@easycoding.org> - 4.2.2-1
- Updated to version 4.2.2.
- Converted SPEC to 201x-era guidelines.

* Tue Dec 07 2021 Vitaly Zaitsev <vitaly@easycoding.org> - 4.2.1-1
- Updated to version 4.2.1.

* Tue Nov 09 2021 Vitaly Zaitsev <vitaly@easycoding.org> - 4.2.0-1
- Updated to version 4.2.0.

* Sun Oct 10 2021 Vitaly Zaitsev <vitaly@easycoding.org> - 4.1.1-1
- Updated to version 4.1.1.

* Sat Sep 25 2021 Vitaly Zaitsev <vitaly@easycoding.org> - 4.1.0-1
- Updated to version 4.1.0.

* Wed Sep 01 2021 Vitaly Zaitsev <vitaly@easycoding.org> - 4.0.0-1
- Updated to version 4.0.0.

* Sat Aug 21 2021 Vitaly Zaitsev <vitaly@easycoding.org> - 3.8.3-1
- Updated to version 3.8.3.

* Thu Jul 22 2021 Vitaly Zaitsev <vitaly@easycoding.org> - 3.8.2-1
- Updated to version 3.8.2.

* Tue Jun 29 2021 Vitaly Zaitsev <vitaly@easycoding.org> - 3.8.1-1
- Updated to version 3.8.1.

* Sun Jun 27 2021 Vitaly Zaitsev <vitaly@easycoding.org> - 3.8.0-2
- Fixed summary field in Python 3 subpackage.

* Sun Jun 27 2021 Vitaly Zaitsev <vitaly@easycoding.org> - 3.8.0-1
- Updated to version 3.8.0.

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 3.7.9-2
- Rebuilt for Python 3.10

* Sun May 16 2021 Vitaly Zaitsev <vitaly@easycoding.org> - 3.7.9-1
- Updated to version 3.7.9.

* Fri Apr 02 2021 Vitaly Zaitsev <vitaly@easycoding.org> - 3.7.7-1
- Updated to version 3.7.7.

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jan 18 2021 Vitaly Zaitsev <vitaly@easycoding.org> - 3.7.6-1
- Updated to version 3.7.6.

* Fri Jan 08 2021 Vitaly Zaitsev <vitaly@easycoding.org> - 3.7.5-1
- Updated to version 3.7.5.

* Sat Nov 21 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 3.7.4-1
- Updated to version 3.7.4.

* Tue Aug 25 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 3.7.3-1
- Updated to version 3.7.3.

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 07 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 3.7.2-1
- Updated to version 3.7.2.

* Wed Jun 24 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 3.6.7-4
- Added python3-setuptools to build requirements.

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 3.6.7-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 27 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 3.6.7-1
- Updated to version 3.6.7.

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 3.6.6-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 3.6.6-4
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Sep 21 2018 Vitaly Zaitsev <vitaly@easycoding.org> - 3.6.6-1
- Updated to version 3.6.6.

* Sat Aug 04 2018 Vitaly Zaitsev <vitaly@easycoding.org> - 3.6.5-1
- Updated to version 3.6.5.

* Fri Aug 03 2018 Vitaly Zaitsev <vitaly@easycoding.org> - 3.6.4-1
- Updated to version 3.6.4.

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jul 02 2018 Vitaly Zaitsev <vitaly@easycoding.org> - 3.6.3-3
- Fixed build under Python 3.7.

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 3.6.3-2
- Rebuilt for Python 3.7

* Tue May 15 2018 Vitaly Zaitsev <vitaly@easycoding.org> - 3.6.3-1
- Updated to version 3.6.3.

* Sat Mar 24 2018 Vitaly Zaitsev <vitaly@easycoding.org> - 3.6.2-1
- Updated to version 3.6.2.

* Mon Mar 12 2018 Vitaly Zaitsev <vitaly@easycoding.org> - 3.6.1-1
- Updated to version 3.6.1.

* Fri Mar 02 2018 Vitaly Zaitsev <vitaly@easycoding.org> - 3.6.0-1
- Updated to version 3.6.0.

* Sat Feb 03 2018 Vitaly Zaitsev <vitaly@easycoding.org> - 3.5.2-1
- Updated to version 3.5.2.

* Fri Dec 01 2017 Vitaly Zaitsev <vitaly@easycoding.org> - 3.5.1-1
- Updated to version 3.5.1.

* Wed Aug 23 2017 Vitaly Zaitsev <vitaly@easycoding.org> - 3.2.0-2
- Small SPEC fixes.

* Tue Aug 22 2017 Vitaly Zaitsev <vitaly@easycoding.org> - 3.2.0-1
- Initial SPEC release.
