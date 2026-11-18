%global common_description %{expand:
DB-IP Lite databases are free IP geolocation databases in the MaxMind DB
(mmdb) format, comparable to, but less accurate than, the commercial DB-IP.com
databases. They can be read by any software that uses libmaxminddb.

IP Geolocation by DB-IP (https://db-ip.com).}

Name:           dbip-lite
Version:        2026.11
Release:        1%{?dist}
Summary:        Free IP geolocation databases from DB-IP

# Upstream versions the files as YYYY-MM; RPM versions cannot contain '-'.
%global upstream_version %{gsub %{version} %. -}

License:        CC-BY-4.0
URL:            https://db-ip.com/db/lite.php
Source0:        https://download.db-ip.com/free/dbip-asn-lite-%{upstream_version}.mmdb.gz
Source1:        https://download.db-ip.com/free/dbip-city-lite-%{upstream_version}.mmdb.gz
Source2:        https://download.db-ip.com/free/dbip-country-lite-%{upstream_version}.mmdb.gz
# The downloads ship without any license text; these carry the attribution
# notice required by upstream and the license legal code (a copy of
# https://creativecommons.org/licenses/by/4.0/legalcode.txt).
Source3:        COPYRIGHT.txt
Source4:        CC-BY-4.0.txt
BuildArch:      noarch

# For the sanity check in %%check
BuildRequires:  /usr/bin/mmdblookup


%description %{common_description}


%package asn
Summary:        Free IP to ASN database from DB-IP


%description asn %{common_description}

This package contains the IP to ASN Lite database.


%package city
Summary:        Free IP to City database from DB-IP


%description city %{common_description}

This package contains the IP to City Lite database.


%package country
Summary:        Free IP to Country database from DB-IP


%description country %{common_description}

This package contains the IP to Country Lite database.


%prep
%setup -q -c -T
gzip -dc %{SOURCE0} > dbip-asn-lite.mmdb
gzip -dc %{SOURCE1} > dbip-city-lite.mmdb
gzip -dc %{SOURCE2} > dbip-country-lite.mmdb
cp -p %{SOURCE3} %{SOURCE4} .


%install
for db in asn city country; do
    install -D -p -m 0644 dbip-$db-lite.mmdb %{buildroot}%{_datadir}/GeoIP/dbip-$db-lite.mmdb
done


%check
# Make sure every database opens and answers lookups.  Locations of a given
# address change between monthly releases, so only check the result shape for
# the location databases.
mmdblookup -f dbip-asn-lite.mmdb -i 8.8.8.8 autonomous_system_number | grep -q '15169 <uint32>'
for db in city country; do
    for ip in 8.8.8.8 2001:4860:4860::8888; do
        mmdblookup -f dbip-$db-lite.mmdb -i $ip country iso_code | grep -Eq '"[A-Z]{2}" <utf8_string>'
    done
done
mmdblookup -f dbip-city-lite.mmdb -i 8.8.8.8 city names en | grep -q '<utf8_string>'


%files asn
%license COPYRIGHT.txt CC-BY-4.0.txt
%dir %{_datadir}/GeoIP
%{_datadir}/GeoIP/dbip-asn-lite.mmdb


%files city
%license COPYRIGHT.txt CC-BY-4.0.txt
%dir %{_datadir}/GeoIP
%{_datadir}/GeoIP/dbip-city-lite.mmdb


%files country
%license COPYRIGHT.txt CC-BY-4.0.txt
%dir %{_datadir}/GeoIP
%{_datadir}/GeoIP/dbip-country-lite.mmdb


%changelog
* Thu Nov 12 2026 Nikos Mavrogiannopoulos <n.mavrogiannopoulos@outlook.com> - 2026.11-1
- Initial package
