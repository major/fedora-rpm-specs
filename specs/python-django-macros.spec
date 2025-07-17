%global srcname django-macros
%global sum Macros for Django templates
%global sum_sv Makron för Djangomallar

Name:           python-%srcname
Version:        0.4.0
Release:        %autorelease
Summary:        %sum
Summary(sv):    %sum_sv

License:        MIT
URL:            https://pypi.python.org/pypi/%srcname
Source0:        https://files.pythonhosted.org/packages/source/d/%srcname/%srcname-%version.zip

BuildArch:      noarch

BuildRequires:  dos2unix
BuildRequires:  python3-devel

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

%generate_buildrequires
%pyproject_buildrequires 

%prep
%autosetup -n %srcname-%version
dos2unix -- README.rst 

%build
%pyproject_wheel

%install
%pyproject_install

%files -n python3-%srcname
%doc README.rst
%license LICENSE
%python3_sitelib/macros
%python3_sitelib/django_macros-%version.dist-info


%changelog
%autochangelog
