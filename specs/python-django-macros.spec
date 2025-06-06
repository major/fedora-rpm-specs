%global srcname django-macros
%global sum Macros for Django templates
%global sum_sv Makron för Djangomallar

Name:           python-%srcname
Version:        0.4.0
Release:        32%{?dist}
Summary:        %sum
Summary(sv):    %sum_sv

License:        MIT
URL:            https://pypi.python.org/pypi/%srcname
Source0:        https://files.pythonhosted.org/packages/source/d/%srcname/%srcname-%version.zip

BuildArch:      noarch

BuildRequires:  dos2unix
BuildRequires:  python3-devel
BuildRequires:  %{py3_dist setuptools}

%description
Macros accepting positional and keyword arguments, and repeated block
tags in the django template system.  Sometimes include tags just do
not get the job done.  Either you have repeated code that you want to
keep all in the same single template, or your code needs to
dynamically generate and substitute in certain values, in a way that
the include syntax inhibits.  Whatever the case, if you are finding
that the built in include tag just is not working for your use case,
then perhaps django-macros is for you.

%description -l sv
Makron som accepterar positions- och nyckelordsargument, och upprepade
blocktaggar i djangos mallsystem.  Ibland får inte include-taggar
jobbet gjort.  Antingen har du upprepad kod som du vill hålla samman i
en mall, eller så behöver din kod dynamiskt generera och substituera
in vissa värden, på ett sätt som include-syntaxen förhindrar.  Oavsett
vilket som är fallet, om du märker att den inbyggda include-taggen
helt enkelt inte fungerar i ditt fall så kanske django-macros är
något för dig.

%package -n python3-%srcname
Summary:        %sum
Summary(sv):    %sum_sv

%?python_enable_dependency_generator

Obsoletes:      python2-%srcname < 0.4.0-4

%{?python_provide:%python_provide python3-%srcname}

%description -n python3-%srcname
Macros accepting positional and keyword arguments, and repeated block
tags in the django template system.  Sometimes include tags just do
not get the job done.  Either you have repeated code that you want to
keep all in the same single template, or your code needs to
dynamically generate and substitute in certain values, in a way that
the include syntax inhibits.  Whatever the case, if you are finding
that the built in include tag just is not working for your use case,
then perhaps django-macros is for you.

%description -l sv -n python3-%srcname
Makron som accepterar positions- och nyckelordsargument, och upprepade
blocktaggar i djangos mallsystem.  Ibland får inte include-taggar
jobbet gjort.  Antingen har du upprepad kod som du vill hålla samman i
en mall, eller så behöver din kod dynamiskt generera och substituera
in vissa värden, på ett sätt som include-syntaxen förhindrar.  Oavsett
vilket som är fallet, om du märker att den inbyggda include-taggen
helt enkelt inte fungerar i ditt fall så kanske django-macros är
något för dig.

%prep
%autosetup -n %srcname-%version
dos2unix -- README.rst 

%build
%py3_build

%install
%py3_install

%files -n python3-%srcname
%doc README.rst
%license LICENSE
%python3_sitelib/macros
%python3_sitelib/django_macros-%version-py%python3_version.egg-info


%changelog
* Mon Jun 02 2025 Python Maint <python-maint@redhat.com> - 0.4.0-32
- Rebuilt for Python 3.14

* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.4.0-29
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 0.4.0-25
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.4.0-22
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-20
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.4.0-19
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.4.0-16
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.4.0-14
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.4.0-13
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 19 2018 Göran Uddeborg <goeran@uddeborg.se> - 0.4.0-10
- Test code removed, as python-django-setuptest is no longer in Fedora.

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.4.0-8
- Rebuilt for Python 3.7

* Tue Feb 13 2018 Göran Uddeborg <goeran@uddeborg.se> - 0.4.0-7
- Remove resudal Python 2 dependency
- Switch to automated Python dependency generator
  (https://fedoraproject.org/wiki/Changes/EnablingPythonGenerators)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Jan 28 2018 Göran Uddeborg <goeran@uddeborg.se> - 0.4.0-5
- Adapt the test code to work with Django 2 (#1537537)

* Mon Jan 22 2018 Göran Uddeborg <goeran@uddeborg.se> - 0.4.0-4
- Remove support for Python 2 (#1494761)
- Add a README file

* Mon Aug 21 2017 Göran Uddeborg <goeran@uddeborg.se> - 0.4.0-3
- Second review round:
- Explain that patch 0 and source 1 are needed for the test suite..
- Fix formatting mistakes in the SPEC file.

* Sat Aug 19 2017 Göran Uddeborg <goeran@uddeborg.se> - 0.4.0-2
- Improvements after review by Robert-André Mauchin:
- Use pyX_dist macros.
- Add a check section and include the necessary build requirements.
- Fix django.template.base.Lexer signature.

* Mon Aug 14 2017 Göran Uddeborg <goeran@uddeborg.se> - 0.4.0-1
- Initial RPM release
