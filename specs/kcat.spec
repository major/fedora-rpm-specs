%global forgeurl https://github.com/edenhill/kcat
Version:         1.7.1
%global ref      %{version}
%forgemeta
Name:            kcat
Release:         7%{?dist}
Summary:         Generic command line non-JVM Apache Kafka producer and consumer

License:         BSD-2-Clause
URL:             %{forgeurl}
Source:          %{forgesource}

BuildRequires:   gcc
BuildRequires:   librdkafka-devel

Provides:        kafkacat = %{version}-%{release}

%description
kcat is a generic non-JVM producer and consumer for Apache Kafka >=0.8, like a
netcat for Kafka.

In producer mode kcat reads messages from stdin, delimited with a configurable
delimiter (-D, defaults to newline), and produces them to the provided Kafka
cluster (-b), topic (-t) and partition (-p).

In consumer mode kcat reads messages from a topic and partition and prints them
to stdout using the configured message delimiter.

There's also support for the Kafka >=0.9 high-level balanced consumer, use the
-G <group> switch and provide a list of topics to join the group.

kcat also features a Metadata list (-L) mode to display the current state of the
Kafka cluster and its topics and partitions.

%prep
%forgesetup
sed -i -e 's/echo $(INSTALL)/$(INSTALL)/g' Makefile


%build
%configure
%make_build


%install
%make_install


%files
%license LICENSE
%doc README.md
%{_bindir}/kcat
%{_mandir}/man1/kcat.1.gz


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Oct 07 2022 Link Dupont <linkdupont@fedoraproject.org> - 1.7.1-1
- Initial package
