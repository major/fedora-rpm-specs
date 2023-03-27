%global forgeurl https://github.com/influxdata/influxdb-client-python

Name:           python-influxdb-client
Version:        1.36.1
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

%package -n python3-influxdb-client
Summary:       %{summary}

%description -n python3-influxdb-client %_description


%prep
%forgesetup

%generate_buildrequires
%pyproject_buildrequires -t


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files influxdb_client


%check
%tox


%files -n python3-influxdb-client -f %{pyproject_files}
%doc README.rst


%changelog
%autochangelog

