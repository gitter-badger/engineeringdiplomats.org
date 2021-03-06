# -*- coding: utf-8 -*-

def apply_routes(app, handler) -> object:
    """Add routes to views, GET is an implied method.
    
    Returns
    -------
    flask.Flask
        Flask application with associated routes.
    """
    # Register GET routes
    app.add_url_rule("/", "index", handler.index)
    app.add_url_rule("/authorize", "authorize", handler.authorize)
    app.add_url_rule("/logout", "logout", handler.logout)
    app.add_url_rule("/resources", "resources", handler.resources)
    
    # Register POST routes
    methods = ["GET", "POST"]
    app.add_url_rule("/login", "login", handler.login, methods=methods)
    app.add_url_rule("/questions", "questions", handler.questions, methods=methods)
    app.add_url_rule("/ask", "ask", handler.ask, methods=methods)
    
    return app