Name:		python-astor
Version:	0.8.1
Release:	%autorelease
Summary:	Designed to allow easy manipulation of python source via the AST

License:	BSD
URL:		https://github.com/berkerpeksag/astor
Source0:	%{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildArch:	noarch
BuildRequires:	python3-devel
BuildRequires:	python3-pytest

%global _description %{expand:
astor is designed to allow easy manipulation of Python source via the AST.}

%description %_description

%package -n python3-astor
Summary:	%{summary}

%description -n python3-astor %_description

%prep
%autosetup -n astor-%{version}
sed -i '/\/usr\/bin\/env.*python/ d' astor/rtrip.py

%generate_buildrequires
%pyproject_buildrequires -r


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files astor


%check
# RtripTestCase.test_convert_stdlib Failed: AssertionError: Lists differ: ['/usr/lib64/python3.10/xml/dom/minidom.py'] != []
# Disable max string length (https://github.com/berkerpeksag/astor/issues/212)
# https://docs.python.org/3/library/stdtypes.html#configuring-the-limit
PYTHONINTMAXSTRDIGITS=0 %pytest -k "not test_convert_stdlib"

%files -n python3-astor -f %{pyproject_files}
%doc README.*


%changelog
%autochangelog
