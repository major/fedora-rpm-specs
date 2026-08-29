%global src_name mako
%global _description %{expand:
Mako is a template library written in Python. It provides a familiar, non-XML
syntax which compiles into Python modules for maximum performance. Mako`s
syntax and API borrows from the best ideas of many others, including Django
templates, Cheetah, Myghty, and Genshi.

Conceptually, Mako is an embedded Python (i.e. Python Server Page) language,
which refines the familiar ideas of componentized layout and inheritance to
produce one of the most straightforward and flexible models available, while
also maintaining close ties to Python calling and scoping semantics.}

Name:		python-%{src_name}
Version:	1.4.1
Release:	%autorelease
Summary:	Mako template library for Python

License:	MIT AND Python-2.0.1 AND BSD-3-Clause
URL:		https://www.makotemplates.org
Source:		https://github.com/sqlalchemy/mako/archive/rel_1_4_1/%{src_name}-%{version}.tar.gz

BuildArch:	noarch

BuildRequires:	python3-devel
BuildRequires:	python3-pytest

%description %{_description}

%package -n python3-%{src_name}
Summary:	%{summary}
%if %{undefined rhel}
# Beaker is the preferred caching backend, but is not strictly necessary
Recommends:	python3-beaker
%endif
Obsoletes:	python2-mako < 1.1.0-3
Obsoletes:	python-mako-doc < 1.1.4-6

%description -n python3-%{src_name} %{_description}

%prep
%autosetup -p1 -n %{src_name}-rel_1_4_1
# fedora doesnt ship lingua
%pyproject_patch_dependency lingua:ignore
%if %{defined rhel}
# not included in RHEL
%pyproject_patch_dependency beaker:ignore
%pyproject_patch_dependency dogpile.cache:ignore
%pyproject_patch_dependency junitparser:ignore
%endif

%generate_buildrequires
%pyproject_buildrequires -g tests

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{src_name}

%check
%pytest -v

%files -n python3-%{src_name} -f %{pyproject_files}
%license LICENSE
%doc CHANGES README.rst examples
%{_bindir}/mako-render

%changelog
%autochangelog
