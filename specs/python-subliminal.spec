%global srcname subliminal

Name:           python-%{srcname}
Version:        2.3.2
Release:        1%{?dist}
Summary:        Python library to search and download subtitles
License:        MIT
URL:            https://github.com/Diaoul/subliminal
Source:         %{pypi_source %{srcname}}
BuildArch:      noarch
BuildRequires:  python3-devel

%global _description %{expand:
Subliminal is a Python library to search and download subtitles.
It comes with an easy to use yet powerful CLI suitable for direct use or
cron jobs.

Subliminal uses multiple providers to give users a vast choice and have
a better chance to find the best matching subtitles. Current supported
providers are:

 - Addic7ed
 - LegendasTV
 - NapiProjekt
 - OpenSubtitles
 - Podnapisi
 - Shooter
 - TheSubDB
 - TvSubtitles}

%description %_description

%package -n python3-%{srcname}
Summary:        %{summary}
Suggests:       %{name}-doc

%description -n python3-%{srcname} %_description

%package doc
Summary:        %summary

%description doc %_description

%prep
%autosetup -p1 -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

%pyproject_save_files -l %{srcname}

pushd docs
# Add folder containing subliminal script to PATH
export SPHINXBUILD=sphinx-build-3
PYTHONPATH=%{buildroot}%{python3_sitelib} PATH=$PATH:%{buildroot}%{_bindir} %make_build html
PYTHONPATH=%{buildroot}%{python3_sitelib} PATH=$PATH:%{buildroot}%{_bindir} %make_build text
PYTHONPATH=%{buildroot}%{python3_sitelib} PATH=$PATH:%{buildroot}%{_bindir} %make_build man
find . -name .buildinfo -type f -delete
popd
install -D -m 0644 docs/_build/man/%{srcname}.1 %{buildroot}%{_mandir}/man1/%{srcname}.1

# Tests disabled because they connect to online services
#%%check
#%%tox

%files -n python3-%{srcname} -f %{pyproject_files}
%{_bindir}/subliminal

%files doc
%doc README.rst docs/_build/html docs/_build/text
%license LICENSE
%{_mandir}/man1/%{srcname}.1*

%changelog
%autochangelog
