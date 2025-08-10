%global srcname Unidecode

Name:		python-unidecode
Version:	1.4.0
Release:	%autorelease
Summary:	US-ASCII transliterations of Unicode text

License:	GPL-2.0-or-later
URL:		https://pypi.python.org/pypi/%{srcname}/%{version}
Source0:	https://files.pythonhosted.org/packages/source/U/%{srcname}/%{srcname}-%{version}.tar.gz

BuildArch:	noarch

%global _description\
This is a python port of Text::Unidecode Perl module. It provides a function,\
'unidecode(...)' that takes Unicode data and tries to represent it in ASCII\
characters.

%description %_description


%package -n python3-unidecode
Summary:	US-ASCII transliterations of Unicode text
BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)

%description -n python3-unidecode
This is a python port of Text::Unidecode Perl module. It provides a function,
'unidecode(...)' that takes Unicode data and tries to represent it in ASCII
characters.


%prep
%autosetup -p1 -n %{srcname}-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install

%pyproject_save_files -l unidecode


%check
%pytest -v


%files -n python3-unidecode -f %{pyproject_files}
%doc README.rst ChangeLog
%{_bindir}/unidecode


%changelog
%autochangelog
