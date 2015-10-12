#!/usr/bin/env python
# -*- coding: UTF-8 -*-


import xmlrpc.client
# import urllib2


class WebFactionAPI:

    def __init__(self, username, password, machine=None):
        super().__init__()
        self.username = username
        self.password = password
        self.machine = machine

    def connect(self):
        self.server = xmlrpc.client.ServerProxy('https://api.webfaction.com/')
        (self._session_id, self._account) = self.server.login(self.username, self.password)

    def create_mailbox(
            self,
            mailbox,
            enable_spam_protection=True,
            discard_spam=False,
            spam_redirect_folder='Junk',
            use_manual_procmailrc=False,
            manual_procmailrc=''
        ):

        if not isinstance(mailbox, str):
            raise TypeError("'mailbox' must be of type string.")
        if not isinstance(enable_spam_protection, bool):
            raise type("'enable_spam_protection' must be of type boolean")
        if not isinstance(discard_spam, bool):
            raise type("'discard_spam' must be of type boolean")
        if not isinstance(discard_spam, bool):
            raise type("'discard_spam' must be of type boolean")
        if not isinstance(spam_redirect_folder, str):
            raise TypeError("'spam_redirect_folder' must be of type string.")
        if not isinstance(use_manual_procmailrc, bool):
            raise type("'use_manual_procmailrc' must be of type boolean")
        if not isinstance(manual_procmailrc, str):
            raise TypeError("'manual_procmailrc' must be of type string.")

        return self.server.create_mailbox(
            self._session_id,
            mailbox,
            enable_spam_protection,
            discard_spam,
            spam_redirect_folder,
            use_manual_procmailrc,
            manual_procmailrc
        )

    def create_email(
            self,
            email_address,
            targets,
            autoresponder_on=False,
            autoresponder_subject='',
            autoresponder_message='',
            autoresponder_from='',
            script_machine='',
            script_path=''
        ):

        if not isinstance(email_address, str):
            raise TypeError("'email_address' must be of type string.")
        if not isinstance(targets, str):
            raise TypeError("'targets' must be of type string.")
        if not isinstance(autoresponder_subject, str):
            raise TypeError("'autoresponder_subject' must be of type string.")
        if not isinstance(autoresponder_message, str):
            raise TypeError("'autoresponder_message' must be of type string.")
        if not isinstance(autoresponder_from, str):
            raise TypeError("'autoresponder_from' must be of type string.")
        if not isinstance(script_machine, str):
            raise TypeError("'script_machine' must be of type string.")
        if not isinstance(script_path, str):
            raise TypeError("'script_path' must be of type string.")
        if not isinstance(autoresponder_on, bool):
            raise type("'autoresponder_on' must be of type boolean")

        return self.server.create_email(
            self._session_id,
            email_address,
            targets,
            autoresponder_on,
            autoresponder_subject,
            autoresponder_message,
            autoresponder_from,
            script_machine,
            script_path
        )

    def list_mailboxes(self):
        return self.server.list_mailboxes(self._session_id)

    def change_mailbox_password(self, mailbox, password):
        return self.server.change_mailbox_password(
            self._session_id,
            mailbox,
            password
        )

    def list_emails(self):
        return self.server.list_emails(self._session_id)

    def update_email(
            self,
            email_address,
            targets,
            autoresponder_on=False,
            autoresponder_subject='',
            autoresponder_message='',
            autoresponder_from='',
            script_machine='',
            script_path=''
        ):
        return self.server.update_email(
            self._session_id,
            email_address,
            targets,
            autoresponder_on,
            autoresponder_subject,
            autoresponder_message,
            autoresponder_from,
            script_machine,
            script_path
        )
