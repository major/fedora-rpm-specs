%global srcname plaster
%global sum Application configuration settings abstraction layer
%global desc plaster is a loader interface around multiple \
configuration file formats. It exists to define a common API for \
applications to use when they wish to load configuration. The library \
itself does not aim to handle anything except a basic API that \
applications may use to find and load configuration settings. Any \
specific constraints should be implemented in a loader which can be \
registered via an entry point.


Name: python-%{srcname}
Version: 1.1.2
Release: %autorelease
BuildArch: noarch

License: MIT
Summary: %{sum}
URL:     https://github.com/Pylons/%{srcname}
Source0: %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildRequires: make
BuildRequires: python3-devel
BuildRequires: python3-sphinx


%description
%{desc}


%package doc
Summary: Documentation for %{name}


%description doc
Contains the documentation for %{name}.


%package -n python3-%{srcname}
Summary: %{sum}

%description -n python3-%{srcname}
%{desc}


%prep
%autosetup -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires -t

# The plaster docs upstream only build if plaster is installed. Since we are building plaster docs
# from a source checkout, let's insert plaster into the path.
sed -i "s:import plaster:sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))\nimport plaster:" docs/conf.py

# Related to the above, upstream plaster gets the version for the docs by using pkg_resources which
# can only work if plaster is installed. Let's just substitute the version in since we know what it
# is.
sed -i "s/version = pkg_resources.*/version = '%{version}'/" docs/conf.py

# Upstream docs use pylons_sphinx_themes, which isn't packaged for Fedora yet. Let's just convert it
# to use the standard sphinx theme for now.
sed -i "/import pylons_sphinx_themes/d" docs/conf.py
sed -i "/html_theme_path =.*/d" docs/conf.py
sed -i "/html_theme =.*/d" docs/conf.py
sed -i "/.*github_url.*/d" docs/conf.py


%build
make %{?_smp_mflags} -C docs html
rm -rf docs/_build/html/.buildinfo

%pyproject_wheel


%install
%pyproject_install

%pyproject_save_files -l plaster

%check
%tox


%files doc
%license LICENSE.txt
%doc docs/_build/html
%doc CHANGES.rst
%doc README.rst


%files -n python3-%{srcname} -f %{pyproject_files}
%license LICENSE.txt
%doc README.rst


%changelog
%autochangelog
