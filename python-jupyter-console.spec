# Unset -s on python shebang - ensure that extensions installed with pip
# to user locations are seen and properly loaded
%global py3_shebang_flags %(echo %py3_shebang_flags | sed s/s//)

%global srcname jupyter-console
%global srcname_ jupyter_console

Name:           python-%{srcname}
Version:        6.4.4
Release:        %autorelease
Summary:        Jupyter terminal console

License:        BSD
URL:            https://jupyter.org
Source0:        %pypi_source %{srcname_}

BuildArch:      noarch

BuildRequires:  python3-devel

%description
An IPython-like terminal frontend for Jupyter kernels in any language.


%package -n     python3-%{srcname}
Summary:        %{summary}

BuildRequires:  python3dist(pillow)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pyzmq)

%description -n python3-%{srcname}
An IPython-like terminal frontend for Jupyter kernels in any language.


%package -n python-%{srcname}-doc
Summary:        jupyter-console documentation

BuildArch: noarch

BuildRequires:  make
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3dist(sphinx-rtd-theme)
BuildRequires:  python3dist(sphinxcontrib-github-alt)

%description -n python-%{srcname}-doc
Documentation for jupyter-console


%prep
%autosetup -n %{srcname_}-%{version} -p1

# setuptools is used, but only implicitly through pip, not explicitly.
sed -i 's/distutils.core/setuptools/g' setup.py

%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel

# generate html docs
%make_build -C docs html PYTHONPATH="%{pyproject_build_lib}"
mv docs/_build/html .
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%install
%pyproject_install
%pyproject_save_files %{srcname_}

%check
%{pytest} -ra

# assert we can start the console ad run a simple command
export PATH=%{buildroot}%{_bindir}:$PATH
export PYTHONPATH=%{buildroot}%{python3_sitelib}
echo 'exit()' | jupyter-console --simple-prompt

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.md
%{_bindir}/%{srcname}

%files -n python-%{srcname}-doc
%doc html
%license LICENSE


%changelog
%autochangelog
