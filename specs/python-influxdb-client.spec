%global forgeurl https://github.com/influxdata/influxdb-client-python

Name:           python-influxdb-client
Version:        1.48.0
%forgemeta
Release:        %autorelease
Summary:        Python client library for the InfluxDB 2.0 and 1.8+

License:        MIT
URL:            %{forgeurl}
Source:         %{forgesource}

BuildArch:      noarch
BuildRequires:  python3-devel

%global _description\
Use this client library with InfluxDB 2.x and InfluxDB 1.8+. For connecting\
to InfluxDB 1.7 or earlier instances, use the python-influxdb package.\

%description   %_description


%pyproject_extras_subpkg -n python3-influxdb-client ciso async extra


%package -n python3-influxdb-client
Summary:       %{summary}

%description -n python3-influxdb-client %_description


%prep
%forgesetup

# python-aiocsv currently not in Fedora.
# Add to fedora once tests are working
# https://github.com/MKuranowski/aiocsv/issues/33
sed -i "s/'aiocsv[>=]=.*//" setup.py

# Relax some versioning
sed -i "s/'aiohttp[>=]=.*'/'aiohttp'/" setup.py
sed -i "s/'ciso8601[>=]=.*'/'ciso8601'/" setup.py
sed -i "s/'reactivex\s*[>=]=\s*.*'/'reactivex'/" setup.py

%generate_buildrequires
%pyproject_buildrequires -x ciso -x async -x extra


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files influxdb_client


%check
# All tests require an influxdb running on the localhost to connect to.
%pyproject_check_import


%files -n python3-influxdb-client -f %{pyproject_files}
%doc README.md CHANGELOG.md


%changelog
%autochangelog

