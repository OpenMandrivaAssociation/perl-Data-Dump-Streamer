%define realname   Data-Dump-Streamer
%define version   2.09
%define release    %mkrel 2

Name:       perl-%{realname}
Version:    %{version}
Release:    %{release}
License:    GPL or Artistic
Group:      Development/Perl
Summary:    Accurately serialize a data structure as Perl code
Url:        http://search.cpan.org/dist/%{realname}
Source:     http://www.cpan.org/modules/by-module/Data/%{realname}-%{version}.tar.gz
BuildRequires: perl-devel
BuildRequires: perl(B::Deparse)
BuildRequires: perl(B::Utils)
BuildRequires: perl(PadWalker)
BuildRequires: perl(Test::More)
BuildRequires: perl(Text::Abbrev)
BuildRequires: perl(Text::Balanced)
Provides:      perl(Data::Dump::Streamer::_::Printers)
Requires:      perl(B::Utils)
BuildRoot:  %{_tmppath}/%{name}-%{version}

%description
Given a list of scalars or reference variables, writes out their contents in
perl syntax. The references can also be objects. The contents of each variable
is output using the least number of Perl statements as convenient, usually only
one. Self-referential structures, closures, and objects are output correctly.

%prep
%setup -q -n %{realname}-%{version}

%build
echo yes | %{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes README
%{_mandir}/man3/*
%perl_vendorarch/Data
%perl_vendorarch/DDS.pm
%perl_vendorarch/auto/Data
